<!-- PAGE 334 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.69** **Multilevel** **Switch** **Command** **Class,** **version** **1**


The Multilevel Switch Command Class is used to control devices with multilevel capability.


The Multilevel Switch Command Class is an actuator control command class. Refer to Section 2.1.6.


**2.2.69.1** **Multilevel** **Switch** **Set** **Command**


This command is used to set a multilevel value in a supporting device.


The device MAY apply a non-zero duration to the transition from one value to a new value.


Table 2.402: Multilevel Switch Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|
|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|
|Value|Value|Value|Value|Value|Value|Value|Value|



**Value** **(8** **bits)**

The encoding of the Value field MUST be according to Table 2.403

|Value|Table 2.403: Multilevel Switch Set::Value Level|State|
|---|---|---|
|Value|Level|State<br>|
|0 (0x00)|0%|Of|
|1..99<br>(0x01..0x63)|Lowest non-zero level .. 100%|On|
|…|_Reserved_|_Reserved_|
|255 (0xFF)|Restore most recent (non-zero) level.|On|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


The above mapping of the Multilevel Switch Command Class Value to hardware levels allows a controlling device to control a mixed group of Binary Switch and Multilevel Switch devices via Basic Set
commands. Devices implementing the Binary Switch CC turn On or Off while devices implementing
the Multilevel Switch CC sets the specified level.


The values 0x00 and 0xFF are special values which MUST be treated as state control commands
indicating “Off” and “On”, respectively. A supporting device MUST restore the most recent (non-zero)
value in response to the “On” state control command.


A device MAY implement up to 100 hardware levels (including 0). If a device implements less than
100 hardware levels, the hardware levels SHOULD be distributed uniformly over the entire range.


The mapping of command values to hardware levels MUST be monotonous, i.e. a higher value MUST
be mapped to either the same or a higher hardware level. Refer to Section 2.1.6.2.


**2.2.69.2** **Multilevel** **Switch** **Get** **Command**


This command is used to request the status of a multilevel device.


The Multilevel Switch Report command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 333




<!-- PAGE 335 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.404: Multilevel Switch Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|
|Command = SWITCH_MULTILEVEL_GET|Command = SWITCH_MULTILEVEL_GET|Command = SWITCH_MULTILEVEL_GET|Command = SWITCH_MULTILEVEL_GET|Command = SWITCH_MULTILEVEL_GET|Command = SWITCH_MULTILEVEL_GET|Command = SWITCH_MULTILEVEL_GET|Command = SWITCH_MULTILEVEL_GET|



**2.2.69.3** **Multilevel** **Switch** **Report** **Command**


This command is used to advertise the status of a multilevel device.


Table 2.405: Multilevel Switch Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|
|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|
|Value|Value|Value|Value|Value|Value|Value|Value|



**Value** **(8** **bits)**

The encoding of the Value field MUST be according to Table 2.406.

|Value|Table 2.406: Multilevel Switch Report::Value Hardware Level|State|
|---|---|---|
|Value|Hardware Level|State<br>|
|0 (0x00)|0%|Of|
|1..99<br>(0x01..0x63)|Lowest non-zero level .. 100%|On|
|…|_Reserved_|On|
|254 (0xFE)|Unknown|Unknown|
|255 (0xFF)|(100%)|On<br>[Depre-<br>cated]|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


The value 255 (0xFF) has been deprecated as it provides no information on the actual value in the
device. A sending node MUST NOT use the value 255. A receiving node MUST interpret the value
255 as 100%.

The Value field SHOULD advertise the current value of the device hardware; also while in transition
to a new target value.


A controlling device MUST NOT assume that the Value is identical to a value previously issued with
a Set command when a transition has ended.


**2.2.69.4** **Multilevel** **Switch** **Start** **Level** **Change** **Command**


This command is used to initiate a transition to a new level.



Table 2.407: Multilevel Switch Start Level Change Command









|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|
|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|
|Re-<br>served|Up/<br>Down|Ignore Start<br>Level|Reserved|Reserved|Reserved|Reserved|Reserved|
|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|


**Up/Down** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 334




<!-- PAGE 336 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST specify the direction of the level change.


If the Up/Down bit is set to 0 the level change MUST be increasing.


If the Up/Down bit is set to 1 the level change MUST be decreasing.


**Ignore** **Start** **Level** **(1** **bit)**


A receiving device SHOULD respect the start level if the Ignore Start Level bit is 0.


A receiving device MUST ignore the start level if the Ignore Start Level bit is 1.


A controlling device SHOULD set the Ignore Start Level bit to 1.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Start** **Level** **(8** **bits)**

The Start Level field MUST specify the initial level of the level change.


**2.2.69.5** **Multilevel** **Switch** **Stop** **Level** **Change** **Command**


This command is used to stop an ongoing transition.


Table 2.408: Multilevel Switch Stop Level Change Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|
|Command = SWITCH_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_STOP_LEVEL_CHANGE|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 335

---

<!-- PAGE 337 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.70** **Multilevel** **Switch** **Command** **Class,** **version** **2**


The Multilevel Switch Command Class is used to control devices with multilevel capability.


The Multilevel Switch Command Class is an actuator control command class. Refer to Section 2.1.6


**2.2.70.1** **Compatibility** **considerations**


A device supporting Multilevel Switch CC, version 2 MUST support Multilevel Switch CC, version 1.


Version 2 adds a “Duration” parameter to the Multilevel Switch Set and Multilevel Switch Start/Stop
Level Change commands.


Commands not described in Version 2 remain unchanged from Version 1.


**2.2.70.2** **Multilevel** **Switch** **Set** **Command**


This command is used to set a multilevel value in a supporting device.


Table 2.409: Multilevel Switch Set Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|
|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|Command = SWITCH_MULTILEVEL_SET|
|Value|Value|Value|Value|Value|Value|Value|Value|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|



**Value** **(8** **bits)**


Refer to _Multilevel_ _Switch_ _Set_ _Command_ .


**Duration** **(8** **bits)**

The Duration field MUST specify the time that the transition should take from the current value to
the new target value.

A supporting device SHOULD respect the specified Duration value.

The encoding of the Duration field MUST be according to Table 2.9.


The factory default duration SHOULD be the same as the duration used for the _Multilevel_ _Switch_ _Set_
_Command_ .


**2.2.70.3** **Multilevel** **Switch** **Start** **Level** **Change** **Command**


This command is used to initiate a transition to a new level.



Table 2.410: Multilevel Switch Start Level Change Command, version 2









|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|
|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|
|Re-<br>served|Up/<br>Down|Ignore Start<br>Level|Reserved|Reserved|Reserved|Reserved|Reserved|
|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|


**Up/Down** **(1** **bit)**

This field MUST specify the direction of the level change.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 336




<!-- PAGE 338 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If the Up/Down bit is set to 0 the level change MUST be increasing.


If the Up/Down bit is set to 1 the level change MUST be decreasing.


**Ignore** **Start** **Level** **(1** **bit)**


A receiving device SHOULD respect the start level if the Ignore Start Level bit is 0.


A receiving device MUST ignore the start level if the Ignore Start Level bit is 1.


A controlling device SHOULD set the Ignore Start Level bit to 1.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Start** **Level** **(8** **bits)**

The Start Level field MUST specify the initial level of the level change.


**Duration** **(8** **bits)**


The dimming rate to use MUST be calculated to match a transition from 0 to 99 during the time
specified by the Duration field.

A supporting device SHOULD respect the specified Duration value.


For encoding of the duration value refer to Section 2.2.70.2.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 337

---

<!-- PAGE 339 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.71** **Multilevel** **Switch** **Command** **Class,** **version** **3**


**Warning:** **The** **Secondary** **Switch** **Type** **of** **the** **Multilevel** **Switch** **Command** **Class,**
**version** **3** **has** **been** **DEPRECATED.**


**The** **Primary** **Switch** **Type** **0x00,** **indicating** **“Not** **supported”,** **of** **the** **Multilevel** **Switch**
**Command** **Class,** **version** **3** **has** **been** **OBSOLETED.**


The implementation of Secondary Switch Type functionality is NOT RECOMMENDED.


While the functionality related to the Secondary Switch Type of the Multilevel Switch Command
Class, version 3 is deprecated, a supporting device claiming compliance with this version MUST
implement support for the Multilevel Switch Supported Get Command.


For backwards compatibility reasons, a device MAY implement Secondary Switch Type functionality. It is however RECOMMENDED that Multi Channel Command Class support is also
implemented if a device provides multiple controllable resources in the same physical entity.


The Multilevel Switch Command Class is used to control devices with multilevel capability.


The Multilevel Switch Command Class is an actuator control Command Class. Refer to Section 2.1.6


Multilevel Switch CC, version 3 adds two-dimensional resource control capabilities to the Multilevel
Switch Start/Stop Level Change commands and introduces two new commands for the discovery of
those capabilities.


The Secondary Switch Type is intended for devices providing two-dimensional control, e.g. Window
blinds, where the Primary Switch Type is used for Up/Down control and the Secondary Switch Type
is used for controlling the slat tilt angle.


The Multilevel Switch Set, Get and Report commands MUST address the primary device functionality.
The Multilevel Switch Start/Stop Level Change commands MUST manipulate the Primary Switch
Type functionality based on the Up/Down parameter.


The Multilevel Switch Start/Stop Level Change commands MUST manipulate the Secondary Switch
Type functionality based on the Inc/Dec parameter.

If the Secondary Switch Type is 0x00 (Undefined / Not supported), the Multilevel Switch Start/Stop
Level Change (Inc/Dec) command parameter MUST be ignored.


**2.2.71.1** **Compatibility** **considerations**


A device supporting Multilevel Switch CC, version 3 MUST support Multilevel Switch CC, version 2.


A device supporting Multilevel Switch CC, version 3 MUST implement the Primary Switch type.


Commands not described in Version 3 remain unchanged from Version 2.


**2.2.71.2** **Multilevel** **Switch** **Supported** **Get** **Command**


This command is used to request the supported Switch Types of a supporting device.


The Multilevel Switch Supported Report command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 338




<!-- PAGE 340 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.411: Multilevel Switch Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|
|Command = SWITCH_MULTILEVEL_SUPPORTED_GET|Command = SWITCH_MULTILEVEL_SUPPORTED_GET|Command = SWITCH_MULTILEVEL_SUPPORTED_GET|Command = SWITCH_MULTILEVEL_SUPPORTED_GET|Command = SWITCH_MULTILEVEL_SUPPORTED_GET|Command = SWITCH_MULTILEVEL_SUPPORTED_GET|Command = SWITCH_MULTILEVEL_SUPPORTED_GET|Command = SWITCH_MULTILEVEL_SUPPORTED_GET|



**2.2.71.3** **Multilevel** **Switch** **Supported** **Report** **Command**


This command is used to advertise the supported Switch Types implemented by a supporting device.


Table 2.412: Multilevel Switch Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|
|Command = SWITCH_MULTILEVEL_SUPPORTED_REPORT|Command = SWITCH_MULTILEVEL_SUPPORTED_REPORT|Command = SWITCH_MULTILEVEL_SUPPORTED_REPORT|Command = SWITCH_MULTILEVEL_SUPPORTED_REPORT|Command = SWITCH_MULTILEVEL_SUPPORTED_REPORT|Command = SWITCH_MULTILEVEL_SUPPORTED_REPORT|Command = SWITCH_MULTILEVEL_SUPPORTED_REPORT|Command = SWITCH_MULTILEVEL_SUPPORTED_REPORT|
|Reserved|Reserved|Reserved|Primary Switch Type|Primary Switch Type|Primary Switch Type|Primary Switch Type|Primary Switch Type|
|Reserved|Reserved|Reserved|Secondary Switch Type|Secondary Switch Type|Secondary Switch Type|Secondary Switch Type|Secondary Switch Type|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Primary** **Switch** **Type** **(5** **bits)**

The Primary Switch Type field MUST represent the primary device functionality.


**Warning:** **Primary** **Switch** **Type** **0x00,** **indicating** **“Not** **supported”,** **has** **been** **OBSO-**
**LETED.**

Previous revisions of this specification allowed that a device may (theoretically) be implemented
with no primary device functionality, i.e. Primary Switch Type 0x00, and specified that such a
device should indicate this situation by returning Multilevel Switch Report commands carrying
the value 0xFE. The value 0xFE is incompatible with Versions 1 and 2 of the Multilevel Switch
Command Class and MUST NOT be used in a Multilevel Switch Report.


The Primary Switch Type MUST comply with Table 2.413.


A supporting device MUST implement the Primary Switch type.


The Primary Switch Type SHOULD be 0x02 (Up/Down).

The Primary Switch Type MUST NOT be 0x00 (Undefined).



Table 2.413: Encoding of Primary and Secondary Switch Types






|Switch Value<br>Type|0x00 (Direction/Endpoint A)|0x63/0xFF (Direction/Endpoint B)|
|---|---|---|
|0x00|Undefned / Not supported (Secondary only)<br>|Undefned / Not supported (Secondary only)<br>|
|0x01|Of|On|
|0x02|Down|Up|
|0x03|Close|Open|
|0x04|Counter-Clockwise|Clockwise|
|0x05|Left|Right|
|0x06|Reverse|Forward|
|0x07|Pull|Push|
|0x08-0x1F|Reserved|Reserved|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Secondary** **Switch** **Type** **(5** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 339




<!-- PAGE 341 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The Secondary Switch Type field MUST represent the secondary device functionality. The Secondary
Switch Type MUST comply with Table 2.413.


A supporting device MAY implement the Secondary Switch type.


**2.2.71.4** **Multilevel** **Switch** **Start** **Level** **Change** **Command**


This command is used to initiate a transition to a new level.


The Multilevel Switch Command Class, version 3 adds a “Secondary Switch Inc/Dec” and a “Secondary Switch Step Size” field to this command to support motor controlled devices featuring
two-dimensional motion.



Table 2.414: Multilevel Switch Start Level Change Command, ver








|7|Table 2.41 sion 3 6|14: Multilevel Swi 5|itch Start Leve 4|vel Change Com 3|mmand, ve 2|er- 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|
|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_MULTILEVEL_START_LEVEL_CHANGE|
|Primary Switch<br>Up/Down|Primary Switch<br>Up/Down|Ignore Start<br>Level|Secondary Switch<br>Inc/Dec|Secondary Switch<br>Inc/Dec|Reserved|Reserved|Reserved|
|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|
|Secondary Switch Step Size|Secondary Switch Step Size|Secondary Switch Step Size|Secondary Switch Step Size|Secondary Switch Step Size|Secondary Switch Step Size|Secondary Switch Step Size|Secondary Switch Step Size|


**Primary** **Switch** **Up/Down** **(2** **bits)**

The Up/Down field MUST be used for manipulating the primary device functionality.

This field MUST be encoded according to Table 2.415.

|Value|Table 2.415: Description|Encoding of the Up/Down field Details|
|---|---|---|
|Value|Description|Details|
|0x00|Up|Increase level for Primary Switch Type|
|0x01|Down|Decrease level for Primary Switch Type|
|0x02|_Reserved_||
|0x03|No Up/Down motion|Maintain current level for Primary Switch Type|



**Ignore** **Start** **Level** **(1** **bit)**


A receiving device SHOULD respect the start level if the Ignore Start Level bit is 0.


A receiving device MUST ignore the start level if the Ignore Start Level bit is 1.


**Secondary** **Switch** **Inc/Dec** **(2** **bits)**

The Inc/Dec field MUST be used for controlling the secondary device functionality.

If the Secondary Switch Type is 0x00 (Undefined / Not supported), the Inc/Dec field MUST be
ignored.

This field MUST be encoded according to Table 2.416.


Table 2.416: Encoding of the Inc/Dec field

|Value|Description|Details|
|---|---|---|
|0x00|Increment|Increase level for Secondary Switch Type|
|0x01|Decrement|Decrease level for Secondary Switch Type|
|0x02|_Reserved_||
|0x03|No Inc/Dec|Maintain current level for Secondary Switch Type|



As this field defines the value “00” of two previously reserved bits as the code “Increment”, a supporting
device implementing Multilevel Switch CC, version 3 MUST correctly identify the Multilevel Switch


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 340




<!-- PAGE 342 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Start Level Change command to be version 3 (by the presence of the <Secondary Switch Step Size>
field) before interpreting the <Secondary Switch Inc/Dec> field. Failing to do so will cause a device
to start incrementing the Secondary Switch Type in response to version 1 and version 2 variants of
the Multilevel Switch Start Level Change command.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Primary** **Switch** **Start** **Level** **(8** **bits)**

The Start Level field MUST be used for controlling the primary device functionality.


**Duration** **(8** **bits)**

This field is unchanged from version 2.


**Secondary** **Switch** **Step** **Size** **(8** **bits)**

The Step Size field MAY be used for controlling a secondary device functionality.

If the Secondary Switch Type is 0x00 (Undefined / Not supported), the Step Size field MUST be
ignored. If the Secondary Switch Type is not 0x00, the Step Size field MUST be used for controlling
the secondary device functionality.

If the Inc/Dec field is set to 3 (No Inc/Dec), the Step Size field MUST be set to 0.

This field MUST carry a value in the range {0x00..0x63, 0xFF}. All other values are reserved and
MUST NOT be used by a sending node. Reserved values MUST be ignored by a receiving node.


A receiving device MUST accept any of the values in the above range. 0x01 MUST represent the
lowest non-zero level and 0x63 MUST represent the highest level


A device MAY implement 100 hardware levels (including 0). If a device implements less than 100
hardware levels, the mapping to hardware levels SHOULD be distributed equally over the entire range
of 1..99 (0x01..0x63).


The mapping of command values to hardware levels MUST be monotonous, i.e. a higher value MUST
be mapped to either the same or a higher hardware level.

An implementation MUST interpret the combined Inc/Dec and Step Size fields as outlined in Table
85.



Table 2.417: Interpretation of the Inc/Dec and Step Size fields






|(Secondary<br>Switch<br>Type)|Inc/Dec|Step Size|Interpretation|
|---|---|---|---|
|_(undefned)_|_(ignore)_|_(ignore)_|Secondary Switch Type is undefned -> ignore felds|
|0x01..0x07|No Inc/Dec|_(ignore)_|No Inc/Dec -> Maintain current Secondary Switch<br>level|
|0x01..0x07|Increment|x|Increase Secondary Switch level by x steps|
|0x01..0x07|Decrement|y|Decrease Secondary Switch level by y steps|



The requested level change SHOULD take the time specified by the Duration field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 341

---

<!-- PAGE 343 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.72** **Multilevel** **Switch** **Command** **Class,** **version** **4**


The Multilevel Switch Command Class is used to control devices with multilevel capability.


The Multilevel Switch Command Class is an actuator control Command Class. Refer to Section 2.1.6.


**2.2.72.1** **Compatibility** **considerations**


Version 4 adds reporting of target value and duration.


A device supporting Multilevel Switch CC, Version 4 MUST support Multilevel Switch CC, Version
3.


A device receiving a V1 Multilevel Set command MAY apply a factory default duration to the transition to a new value.


**2.2.72.2** **Multilevel** **Switch** **Report** **Command**


This command is used to advertise the status of a multilevel device.


Table 2.418: Multilevel Switch Report Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_MULTILEVEL|
|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|Command = SWITCH_MULTILEVEL_REPORT|
|Current Value|Current Value|Current Value|Current Value|Current Value|Current Value|Current Value|Current Value|
|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|



**Current** **Value** **(8** **bits)**

The encoding of the Value field MUST be according to Table 2.406.


The device may be queried for its current value while in transition to a new value. The response to a
Get command SHOULD be the current value of the device hardware.


A controlling device MUST NOT assume that the Value is identical to a value previously issued with
a Set command when a transition has ended.


**Target** **Value** **(8** **bits)**

The Target Value field MUST advertise the target value of an ongoing transition or the most recent
transition.

The encoding of the Target Value field MUST be according to Table 2.406.

If queried after receiving a Set command, the Target Value field MUST advertise the target value
specified in the Set command. The Target Value may change at a later time due to local control or a
Multilevel Switch Stop Level Change command.

If the device is in a motion controlled transition, the Target Value field MUST advertise the value
0x00 or 0x63.


**Duration** **(8** **bits)**

The Duration field SHOULD advertise the time needed to reach the Target Value at the actual
transition rate. The encoding of the Duration field MUST be according to Table 2.9.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 342