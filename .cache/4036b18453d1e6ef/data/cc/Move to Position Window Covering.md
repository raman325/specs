<!-- PAGE 321 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.66** **Move** **to** **Position** **Window** **Covering** **Command** **Class,** **version** **1**


**Warning:** THIS COMMAND CLASS HAS BEEN OBSOLETED


New implementations MUST NOT support this command class.


Window covering device implementations SHOULD support the Window Covering Command
Class.


The Move To Position Window Covering Command Class is used to control the position of a window
covering device.


The Move To Position Window Covering Command Class is an actuator control command class. Refer
to Section 2.1.6


**2.2.66.1** **Move** **To** **Position** **Set** **Command**


This command is used to instruct a window covering to move to a new position.


Table 2.387: Move To Position Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|
|Command = MOVE_TO_POSITION_SET|Command = MOVE_TO_POSITION_SET|Command = MOVE_TO_POSITION_SET|Command = MOVE_TO_POSITION_SET|Command = MOVE_TO_POSITION_SET|Command = MOVE_TO_POSITION_SET|Command = MOVE_TO_POSITION_SET|Command = MOVE_TO_POSITION_SET|
|Value|Value|Value|Value|Value|Value|Value|Value|



**Value** **(8** **bits)**

The encoding of the Value field MUST be according to Table 2.388.


Table 2.388: Move To Position Set::Value

|Value|Level|State|
|---|---|---|
|0 (0x00)|0%|Closed|
|1..99 (0x01..0x63)|Almost closed .. 100% Open|Open|
|…|_Reserved_|_Reserved_|
|255 (0xFF)|100% Open|Open|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**2.2.66.2** **Move** **To** **Position** **Get** **Command**


This command is used to request the status of a window covering device.


The Move To Position Report command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.389: Move To Position Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|
|Command = MOVE_TO_POSITION_GET|Command = MOVE_TO_POSITION_GET|Command = MOVE_TO_POSITION_GET|Command = MOVE_TO_POSITION_GET|Command = MOVE_TO_POSITION_GET|Command = MOVE_TO_POSITION_GET|Command = MOVE_TO_POSITION_GET|Command = MOVE_TO_POSITION_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 320




<!-- PAGE 322 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.66.3** **Move** **To** **Position** **Report** **Command**


This command is used to advertise the status of a window covering device.


Table 2.390: Move To Position Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|Command Class = COMMAND_CLASS_MTP_WINDOW_COVERING|
|Command = MOVE_TO_POSITION_REPORT|Command = MOVE_TO_POSITION_REPORT|Command = MOVE_TO_POSITION_REPORT|Command = MOVE_TO_POSITION_REPORT|Command = MOVE_TO_POSITION_REPORT|Command = MOVE_TO_POSITION_REPORT|Command = MOVE_TO_POSITION_REPORT|Command = MOVE_TO_POSITION_REPORT|
|Value|Value|Value|Value|Value|Value|Value|Value|



**Value** **(8** **bits)**

The encoding of the Value field MUST be according to Table 2.388.

The Value field SHOULD advertise the current value of the device hardware; also while in transition
to a new target value.


A controlling device MUST NOT assume that the Value is identical to a value previously issued with
a Set command when a transition has ended.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 321




<!-- PAGE 323 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.67** **Multilevel** **Sensor** **Command** **Class,** **version** **1-4**


The Multilevel Sensor Command Class is used to advertise numerical sensor readings..


**2.2.67.1** **Multilevel** **Sensor** **Get** **Command**


This command is used to request the current reading from a multilevel sensor.


CC:0031.01.04.11.001 The Multilevel Sensor Report Command MUST be returned in response to this command.


CC:0031.01.04.11.002 This command MUST NOT be issued via multicast addressing.


CC:0031.01.04.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.391: Multilevel Sensor Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|
|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|



**2.2.67.2** **Multilevel** **Sensor** **Report** **Command**


This command is used by a supporting node to advertise its current sensor reading for its supported
sensor type.


Table 2.392: Multilevel Sensor Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|
|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|
|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Sensor Value 1|Sensor Value 1|Sensor Value 1|Sensor Value 1|Sensor Value 1|Sensor Value 1|Sensor Value 1|Sensor Value 1|
|…|…|…|…|…|…|…|…|
|Sensor Value N|Sensor Value N|Sensor Value N|Sensor Value N|Sensor Value N|Sensor Value N|Sensor Value N|Sensor Value N|



**Sensor** **Type** **(8** **bits)**

This field is used to specify the sensor type of the actual sensor reading.

CC:0031.01.05.11.001 This field MUST be set to a value defined in [27]. Values not defined in [27] are reserved and MUST
NOT be used.


CC:0031.01.05.11.002 A node MUST support as a minimum the highest Multilevel Sensor Command Class version associated
with the Scale and Type it supports. The minimum required version for each Scale and Type is
specified in [27].


**Precision** **(3** **bits)**

This field is used to indicate how many decimal places are included the Sensor Value field. For
CC:0031.01.05.11.003 example, the Sensor Value 1025 with precision 2 MUST be interpreted as equal to 10.25.


**Scale** **(2** **bits)**

This field is used to indicate what scale is used for the actual sensor reading.

CC:0031.01.05.11.004 This field MUST be set to a value defined in [27]. Values not defined in [27] are reserved and MUST
NOT be used.


CC:0031.01.05.11.005 A node MUST implement as a minimum the highest Multilevel Sensor Command Class version associated with the Scale and Type it supports. The minimum required version for each Scale and Type
is specified in [27].


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 322




<!-- PAGE 324 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Size** **(3** **bits)**

This field is used to indicate the length in bytes of the Sensor Value field.

CC:0031.01.05.11.006 This field MUST be set to 1, 2 or 4.


**Sensor** **Value** **(N** **bytes)**

This field is used to advertise the value of the actual sensor reading.

CC:0031.01.05.11.007 The length of this field in bytes MUST be according to the Size field value.

CC:0031.01.05.11.008 The first byte MUST be the most significant byte.

CC:0031.01.05.11.009 This field MUST be encoded using signed representation and comply with Table 2.12, Signed field
encoding (two’s complement representation).


CC:0031.01.05.11.00A A controlling node receiving this command MUST always show the sensor value as is even though the
Sensor Type and/or Scale are unknown.



CC:0031.01.05.12.001


CC:0031.01.05.12.002



A controlling node SHOULD implement the capability to update its list of Sensor Type and Scales, so
that new Sensor Types and Scales added in [27] are not presented as unknown. If a controlling node
receives an unknown Sensor Type or Scale, it SHOULD allow the user to assign a free-text description
to the sensor reading.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 323




<!-- PAGE 325 -->

CC:0031.05.05.22.001


CC:0031.05.05.22.002



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.68** **Multilevel** **Sensor** **Command** **Class,** **version** **5-11**


The Multilevel Sensor Command Class is used to advertise numerical sensor readings .


**2.2.68.1** **Compatibility** **considerations**


A node supporting version 5 or newer may support several sensor types and advertise the readings for
each of them.


Version 5 of this command class is extended with the following functionality:


 - A “get-supported” mechanism for the controlling device to interview the multilevel sensor for
its supported sensor types and/or scales

 - Additional sensor type and scale fields to the Multilevel Sensor Get command to request for a
specific sensor report


 - Additional sensor types and/or scales to the list of multilevel sensors


Version 6 of this command class is extended with the following functionality:


 - Additional sensor types


Version 7 of this command class is extended with the following functionality:


 - Additional sensor types


Version 8 of this command class is extended with the following functionality:


 - New Sensor Types and Scale Values for rotation and linear movement.


 - New Sensor Types and Scale Values for Smoke Density


Multilevel Sensor Command Class, version 8 deprecates the Sensor Type “Angle Position”.


Version 9 of this command class is extended with the following functionality:


 - New Sensor Types and Scale Values for Water Flow and Water Pressure


 - New Sensor Types and Scale Values for RF Signal Strength


Version 10 of this command class is extended with the following functionality:


 - New Sensor Types and Scale Values for Particulate Matter 10 and Respiratory rate


 - New Scale Values for CO and VOC Sensors Types


Version 11 of this command class is extended with the following functionality:


 - New Sensor Types and Scale Values.


 - Moved the list of assigned Sensor Types and Scale Values to an external registry [27].


 - Deprecated the “General Purpose” Sensor Type


**2.2.68.1.1** **Unknown** **Multilevel** **Sensor** **Types** **and** **Scales**


A controlling node SHOULD implement the capability to update its Multilevel sensor types and scales
list, so that new Types and Scales added in [27] are not presented as unknown. If a controlling node
receives an unknown Type or Scale, it SHOULD allow the user to assign a free-text description to
that Type or Scale.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 324




<!-- PAGE 326 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.68.2** **Multilevel** **Sensor** **Get** **Supported** **Sensor** **Command**


This command is used to request the supported Sensor Types from a supporting node.


CC:0031.05.01.11.001 The Multilevel Sensor Supported Sensor Report Command MUST be returned in response to this
command.


CC:0031.05.01.11.002 This command MUST NOT be issued via multicast addressing.


CC:0031.05.01.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.393: Multilevel Sensor Get Supported Sensor Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|
|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SENSOR|



**2.2.68.3** **Multilevel** **Sensor** **Supported** **Sensor** **Report** **Command**


This command is used to advertise the supported Sensor Types by a supporting node.


Table 2.394: Multilevel Sensor Supported Sensor Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|
|Command = SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SENSOR_REPORT|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Bit** **Mask** **(N** **bytes)**

This field is used to advertise the supported sensor types by sending node.

CC:0031.05.02.11.001 This field MUST be treated as a bit mask and interpreted as follows:


      - Bit 0 in Bit Mask 1 indicates if Sensor Type = Air Temperature (0x01) is supported


      - Bit 1 in Bit Mask 1 indicates if Sensor Type = General Purpose (0x02) is supported


      - Bit 2 in Bit Mask 1 indicates if Sensor Type = luminance (0x03) is supported


      - …

The list of Sensor Types is defined in [27].


CC:0031.05.02.11.002 The value 1 MUST indicate that the corresponding Sensor Type is supported.


The value 0 MUST indicate that the corresponding Sensor Type is not supported.

CC:0031.05.02.11.003 It is only necessary to send the Bit Mask fields from 1 and up to the Bit Mask N indicating the last
supported Sensor Type. The number of Bit Mask fields transmitted MUST be determined from the
length field in the frame.

Note that the mapping of bit 0 to Sensor Type = 1 differs from the support mapping used by the
Notification Command Class. The Notification Command Class maps bit 1 to Notification Type =1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 325




<!-- PAGE 327 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.68.4** **Multilevel** **Sensor** **Get** **Supported** **Scale** **Command**


This command is used to retrieve the supported scales of the specific sensor type from the Multilevel
Sensor device.


CC:0031.05.03.11.001 The Multilevel Sensor Supported Scale Report Command MUST be returned in response to this
command.


CC:0031.05.03.11.002 This command MUST NOT be issued via multicast addressing.


CC:0031.05.03.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.395: Multilevel Sensor Get Supported Scale Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|
|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE|Command = SENSOR_MULTILEVEL_SUPPORTED_GET_SCALE|
|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|



**Sensor** **Type** **(8** **bits)**

This field is used to request a given sensor type.

CC:0031.05.03.12.001 If the specified sensor type is not supported, a receiving node SHOULD set the _Scale_ _Bit_ _Mask_ field
to 0 in the returned response.


**2.2.68.5** **Multilevel** **Sensor** **Supported** **Scale** **Report** **Command**


This command is used to advertise the supported scales of a specified multilevel sensor type.


Table 2.396: Multilevel Sensor Supported Scale Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|
|Command = SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT|Command = SENSOR_MULTILEVEL_SUPPORTED_SCALE_REPORT|
|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|
|Reserved|Reserved|Reserved|Reserved|Scale Bit Mask|Scale Bit Mask|Scale Bit Mask|Scale Bit Mask|



**Sensor** **Type** **(8** **bits)**

This field is used to indicate the actual Sensor Type for which the supported scales are being advertised.


**Scale** **Bit** **Mask** **(4** **bits)**

This field is used to advertise the supported scales for the actual sensor type.

CC:0031.05.06.11.001 This field MUST be treated as a bit mask and interpreted as follow:

      - Bit 0 indicates support for the first scale of the actual Sensor Type


      - Bit 1 indicates support for the second scale of the actual Sensor Type


      - …

The list of scales for a given sensor type is defined in [27].


CC:0031.05.06.11.002 The value 1 MUST indicate that the corresponding scale is supported for the sensor type.


The value 0 MUST indicate that the corresponding scale is not supported for the sensor type.


**Reserved**

CC:0031.05.06.11.003 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 326




<!-- PAGE 328 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.68.6** **Multilevel** **Sensor** **Get** **Command**


This command is used to request the current reading from a multilevel sensor.


CC:0031.05.04.11.001 The Multilevel Sensor Report Command MUST be returned in response to this command.


CC:0031.05.04.11.002 This command MUST NOT be issued via multicast addressing.


CC:0031.05.04.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods


Table 2.397: Multilevel Sensor Get Command, version 5-11

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|
|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|Command = SENSOR_MULTILEVEL_GET|
|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|
|Reserved|Reserved|Reserved|Scale|Scale|Reserved|Reserved|Reserved|



**Sensor** **Type** **(8** **bits)**

This field is used to request a node to report a reading for the specified sensor type.

CC:0031.05.04.11.004 If this field is unspecified or a receiving node does not support the specified Sensor Type, it MUST
reply with a pre-defined default Sensor Type and Scale.


**Scale** **(2** **bits)**

This field is used to request a node to report a reading with a particular scale for the actual Sensor
Type.


CC:0031.05.04.11.005 A node receiving a non-supported scale for the actual Sensor Type MUST reply with a supported
scale within the Sensor type.


CC:0031.05.04.11.006 A sending node MUST ensure that the receiver supports the requested Sensor Types and/or Scales
using the Multilevel Sensor Get Supported Sensor/Scale commands.


**Reserved**

CC:0031.05.04.11.007 These fields MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**2.2.68.7** **Multilevel** **Sensor** **Report** **Command**


This command is used to advertise a multilevel sensor reading.


Table 2.398: Multilevel Sensor Report Command, version 5-11

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|Command Class = COMMAND_CLASS_SENSOR_MULTILEVEL|
|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|Command = SENSOR_MULTILEVEL_REPORT|
|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|Sensor Type|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Sensor Value 1|Sensor Value 1|Sensor Value 1|Sensor Value 1|Sensor Value 1|Sensor Value 1|Sensor Value 1|Sensor Value 1|
|…|…|…|…|…|…|…|…|
|Sensor Value N|Sensor Value N|Sensor Value N|Sensor Value N|Sensor Value N|Sensor Value N|Sensor Value N|Sensor Value N|



**Sensor** **Type** **(8** **bits)**

This field is used to specify the sensor type of the actual sensor reading.

CC:0031.05.05.11.001 This field MUST be set to a value defined in [27]. Values not defined in [27] are reserved and MUST
NOT be used.


CC:0031.05.05.11.002


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 327




<!-- PAGE 329 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A node MUST support as a minimum the highest Multilevel Sensor Command Class version associated
with the Scale and Type it supports. The minimum required version for each Scale and Type is
specified in [27].


**Precision** **(3** **bits)**

This field is used to indicate how many decimal places are included the Sensor Value field. For
CC:0031.05.05.11.003 example, the Sensor Value 1025 with precision 2 MUST be interpreted as equal to 10.25.


**Scale** **(2** **bits)**

This field is used to indicate what scale is used for the actual sensor reading.

CC:0031.05.05.11.004 This field MUST be set to a value defined in [27]. Values not defined in [27] are reserved and MUST
NOT be used.


CC:0031.05.05.11.005 A node MUST implement as a minimum the highest Multilevel Sensor Command Class version associated with the Scale and Type it supports. The minimum required version for each Scale and Type
is specified in [27].


**Size** **(3** **bits)**

This field is used to indicate the length in bytes of the Sensor Value field.

CC:0031.05.05.11.006 This field MUST be set to 1, 2 or 4.


**Sensor** **Value** **(N** **bytes)**

This field is used to advertise the value of the actual sensor reading.

CC:0031.05.05.11.007 The length of this field MUST be according to the Size field value.

CC:0031.05.05.11.008 The first byte MUST be the most significant byte.

CC:0031.05.05.11.009 This field MUST be encoded using signed representation and comply with Table 2.12, Signed field
encoding (two’s complement representation).


CC:0031.05.05.11.00A A controlling node receiving this command MUST always show the sensor value as is even though the
Sensor Type and/or Scale are unknown.



CC:0031.05.05.12.001


CC:0031.05.05.12.002



A controlling node SHOULD implement the capability to update its list of Sensor Type and Scales, so
that new Sensor Types and Scales added in [27] are not presented as unknown. If a controlling node
receives an unknown Sensor Type or Scale, it SHOULD allow the user to assign a free-text description
to the sensor reading.


**2.2.68.7.1** **Detailed** **description:** **Sensor** **Types** **for** **Movement** **and** **Rotation**


A device may report position, velocity (position change over time) or acceleration (velocity change
over time). Position, velocity and acceleration may all refer to a linear scale following an axis or a
polar scale circling an axis. Position may be reported in an absolute or relative fashion.


The 3D reference coordinate system outlined below MUST be used for reporting changes in the
physical orientation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 328




<!-- PAGE 330 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 2.12: 3D reference coordinate system


Information relating to linear position, velocity and acceleration MUST refer to the zero position on a
CC:0031.05.05.11.00B given axis. Thus a position change or a velocity MUST be positive if moving towards a larger position,
measured from the zero position.


CC:0031.05.05.11.00C Information relating to an angle or change in angle MUST use the right-hand rule. This means that
if one (virtually) grabs around an axis with the right hand, with the thumb in the direction of the
axis, the angle increases in the direction of the index finger.


Table 2.399: Definition of position, velocity or acceleration

|Application|i<br>Defnition|
|---|---|
|Linear position, absolute|Position with reference to 0 (e.g. 1 meter)|
|Linear position, relative|Position with reference to previous position (e.g. 1 meter)|
|Linear velocity|Position change per time unit (e.g. 1 meter/second)|
|Linear acceleration|Velocity change per time unit (e.g. 1 meter/second^2)|
|Polar position, absolute|Angle with reference to 0 (e.g. 45 degrees)|
|Polar position, relative|Angle with reference to previous angle (e.g. 45 degrees)|
|Polar velocity (rotation)|Angle change per time unit (e.g. 1 degree/second)|
|Polar acceleration|Velocity change per time unit (e.g. 1 degree/second^2)|



Depending on the number of axes supported by a given device, changes in the physical orientation are
mapped to one, two or three axes as outlined in Table 2.400.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 329




<!-- PAGE 331 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.400: Mapping of 1D, 2D and 3D movement and rotation

|Dimensions|Movement|Rotation|
|---|---|---|
|1|Along X axis|Around X axis|
|2|Along X and Y axes|Around X and Y<br>axes|
|3|Along X, Y and Z axes|Around X, Y and<br>Z axes|



A number of Sensor Types allow a device to report changes in the physical orientation.


Table 2.401: Recommended Sensor Types for reporting movement
and rotation



































|Application|Sensor<br>Type|Intended Usage|
|---|---|---|
|1D Linear posi-<br>tion, absolute|Distance<br>(v3)|Single axis measurement of position (m)|
|1D Linear posi-<br>tion, relative|_(no support)_|Single axis measurement of position change (m)|
|1D Linear veloc-<br>ity|Velocity<br>(v2)|Single axis measurement of velocity (m/s)|
|1D<br>Linear<br>ac-<br>celleration|Acceler-<br>ation,<br>X<br>(v8)|Single axis measurement of acceleration (m/s^2)|
|1D<br>Polar<br>posi-<br>tion, absolute|Direction<br>(v2)|Single axis measurement of angle (degrees)|
|1D<br>Polar<br>posi-<br>tion, relative|_(no support)_|Single axis measurement of angle change|
|1D Polar velocity|Rotation<br>(v5)|Single axis measurement of velocity (RPM)|
|1D<br>Polar<br>ac-<br>celleration|_(no support)_|Single axis measurement of acceleration (degree/s^2)|
|2D Linear posi-<br>tion, absolute|_(no support)_|Two axis measurement of position (m)|
|2D Linear posi-<br>tion, relative|_(no support)_|Two axis measurement of position change (m)|
|2D Linear veloc-<br>ity|_(no support)_|Two axis measurement of velocity (m/s)|
|2D<br>Linear<br>ac-<br>celleration|Acceler-<br>ation,<br>X<br>(v8), Accel-<br>eration,<br>Y<br>(v8)|Two axis measurement of acceleration (m/s^2)|
|2D<br>Polar<br>posi-<br>tion, absolute|_(no support)_|Two axis measurement of angle (degrees from North)|
|2D<br>Polar<br>posi-<br>tion, relative|_(no support)_|Two axis measurement of angle change|
|2D Polar velocity|_(no support)_|Two axis measurement of velocity (RPM)|
|2D<br>Polar<br>ac-<br>celleration|_(no support)_|Two axis measurement of acceleration (degree/s^2)|
|3D Linear posi-<br>tion, absolute|_(no support)_|Three axis measurement of position (m)|
|3D Linear posi-<br>tion, relative|_(no support)_|Three axis measurement of position change (m)|
|3D Linear veloc-<br>ity|_(no support)_|Three axis measurement of velocity (m/s)|


continues on next page



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 330




<!-- PAGE 332 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024












|Application|Table Sensor|2.401 – continued from previous page Intended Usage|
|---|---|---|
|**Application**|**Sensor**<br>**Type**|**Intended Usage**|
|3D<br>Linear<br>ac-<br>celleration|Acceler-<br>ation,<br>X<br>(v8), Accel-<br>eration,<br>Y<br>(v8), Accel-<br>eration,<br>Z<br>(v8)|Three axis measurement of acceleration (m/s^2)|
|3D<br>Polar<br>posi-<br>tion, absolute|_(no support)_|Three axis measurement of angle (degrees from North)|
|3D<br>Polar<br>posi-<br>tion, relative|_(no support)_|Three axis measurement of angle change|
|3D Polar velocity|_(no support)_|Three axis measurement of velocity (RPM)|
|3D<br>Polar<br>ac-<br>celleration|_(no support)_|Three axis measurement of acceleration (degree/s^2)|



**2.2.68.7.2** **Sensor** **Type** **=** **Acceleration**


The sensor types “Acceleration, X”, “Acceleration, Y” and “Acceleration, Z” are used to advertise the
acceleration of a device along the X, Y and Z axes, respectively.


CC:0031.05.05.11.00D A one-dimensional device MUST report acceleration using the “Acceleration, X” type.


CC:0031.05.05.11.00E A two-dimensional device MUST report acceleration using the “Acceleration, X” and “Acceleration,
Y” types.


CC:0031.05.05.11.00F The Scale used MUST be m/s2. An Acceleration value reported with the Scale m/s2 may be converted
by a receiving node to a “g-force” level by using the formula below:


_1g_ _=_ _9.81m/s^2_


_(g_ _represents_ _the_ _unit_ _of_ _Earth_ _Gravity;_ _NOT_ _the_ _weight_ _unit_ _“gram”)_


**2.2.68.7.3** **Detailed** **description:** **Smoke** **Density**


Figure 2.13 shows the principle of how a photoelectric smoke detector works. As shown the smoke
sensor uses the smoke to reflect the light onto a photo cell. So when no smoke is present, the light
will not be reflected onto the photo cell. When smoke is present, the light will be reflected onto the
photo cell. Dependent on the smoke density, more light will be reflected onto the photo cell. So by
measuring the received light strength on the photo cell, it is possible to estimate the smoke density.


It is not possible to determine an accurate unit for this, as it is estimated from the light strength
on the photo cell. So the exact particle density of the smoke is not known. Also the light strength
interval measured on the photo cell, may vary between sensors. So it is decided to report the smoke
density in percent, where 0% is no smoke and 100% is the maximum received light strength on the
photo cell.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 331




<!-- PAGE 333 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 2.13: Photoelectric smoke detector


**2.2.68.7.4** **Detailed** **description:** **RF** **Signal** **Strength**


The RF Signal Strength sensor type may report values using two different scales. While the dBm
is a well-defined unit, the RSSI value represents a relative measurement where the internal sampling
circuits and the actual sampling method is product specific.


CC:0031.05.05.11.010 The RSSI value MUST be reported in the range 0..100, where the value 100 represents the highest
power level that can be measured.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 332