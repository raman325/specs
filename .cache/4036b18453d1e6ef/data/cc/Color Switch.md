<!-- PAGE 144 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.27** **Color** **Switch** **Command** **Class,** **version** **1**


The Color Switch Command Class is used to control color capable devices.


The Color Switch Command Class manipulates the color components of a device. Each color component is scaled by the brightness level previously set by a Multilevel Switch Set, Binary Switch Set or
Basic Set Command.


The Color Switch Command Class is an actuator control command class. Refer to Section 2.1.6.


**2.2.27.1** **Compatibility** **considerations**


The Color Switch Command Class, version 1 was previously named the Color Control Command
Class, version 1. The Color Switch Command Class, version 1 is binary compatible with the Color
Control Command Class, version 1.


**2.2.27.1.1** **Command** **Class** **dependencies**


CC:0033.01.00.21.001 Nodes supporting the Color Switch Command Class, version 1 MUST support one of the following
command classes in order to control the color brightness:


      - Multilevel Switch Command Class, version 2


      - Binary Switch Command Class, version 2.


**2.2.27.2** **Interoperability** **considerations**


CC:0033.01.00.31.001 The Color Switch Command Class MUST be treated as a separate Command Class.

CC:0033.01.00.31.002 Basic and Binary/Multilevel Switch Command Class commands MUST NOT affect color component
levels controlled by the Color Switch Command Class.

CC:0033.01.00.31.003 The Color Switch Command Class commands MUST NOT affect the brightness level controlled by
Basic or Binary/Multilevel Switch Command Classes.


CC:0033.01.00.31.004 If the brightness level is requested via a Basic Get or Binary/Multilevel Switch Get command, the
reported value MUST reflect the brightness level previously set via Basic or Multilevel Switch commands.


CC:0033.01.00.31.005
If a color component is requested via the Color Switch Get command, the reported value MUST reflect
the color component level previously set via Color Switch commands.


CC:0033.01.00.31.006 An implementation MUST scale color component levels by the brightness level . Thus, to achieve a
resulting light level of 100% for a given color component, the color component level must be set to
100% (via the Color Switch Command Class) and the brightness level must be set to 100% (via Basic
or Multilevel Switch Command Class).


CC:0033.01.00.32.001 A controlling device SHOULD specify the highest possible color component levels of a given color tone
to achieve the highest light yield when scaled by the brightness level.


CC:0033.01.00.33.001 The controlling device MAY however limit color component levels to achieve the same brightness for

CC:0033.01.00.31.007 blended color tones as for pure colors. For this reason, a supporting device MUST NOT normalize
color components manipulated by the Color Switch Command Class.


Likewise, a supporting device implementing indexed colors should reduce its internal color component
levels for blended colors to achieve the same brightness for all color tones.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 143




<!-- PAGE 145 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.27.3** **Color** **Switch** **Supported** **Get** **Command**


This command is used to request the supported color components of a device.


CC:0033.01.01.11.001 The Color Switch Supported Report command MUST be returned in response to this command.


CC:0033.01.01.11.002 This command MUST NOT be issued via multicast addressing.


CC:0033.01.01.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.138: Color Switch Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|
|Command = SWITCH_COLOR_SUPPORTED_GET|Command = SWITCH_COLOR_SUPPORTED_GET|Command = SWITCH_COLOR_SUPPORTED_GET|Command = SWITCH_COLOR_SUPPORTED_GET|Command = SWITCH_COLOR_SUPPORTED_GET|Command = SWITCH_COLOR_SUPPORTED_GET|Command = SWITCH_COLOR_SUPPORTED_GET|Command = SWITCH_COLOR_SUPPORTED_GET|



**2.2.27.4** **Color** **Switch** **Supported** **Report** **Command**


This command is used to report the supported color components of a device.


Table 2.139: Color Switch Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|
|Command = SWITCH_COLOR_SUPPORTED_REPORT|Command = SWITCH_COLOR_SUPPORTED_REPORT|Command = SWITCH_COLOR_SUPPORTED_REPORT|Command = SWITCH_COLOR_SUPPORTED_REPORT|Command = SWITCH_COLOR_SUPPORTED_REPORT|Command = SWITCH_COLOR_SUPPORTED_REPORT|Command = SWITCH_COLOR_SUPPORTED_REPORT|Command = SWITCH_COLOR_SUPPORTED_REPORT|
|Color Component Mask 1|Color Component Mask 1|Color Component Mask 1|Color Component Mask 1|Color Component Mask 1|Color Component Mask 1|Color Component Mask 1|Color Component Mask 1|
|Color Component Mask 2|Color Component Mask 2|Color Component Mask 2|Color Component Mask 2|Color Component Mask 2|Color Component Mask 2|Color Component Mask 2|Color Component Mask 2|



**Color** **Component** **Mask** **(variable** **length)**

CC:0033.01.02.11.001 The Color Component Mask field MUST advertise the color components supported by the device.


      - Bit 0 in Bit Mask 1 indicates if color component 0 is supported


      - Bit 1 in Bit Mask 1 indicates if color component 1 is supported


      - …

For the definition of Color Component IDs, refer to section Section 2.2.27.7.


**2.2.27.5** **Color** **Switch** **Get** **Command**


This command is used to request the status of a specified color component.


CC:0033.01.03.11.001 The Color Switch Report Command MUST be returned in response to this command.


CC:0033.01.03.11.002 This command MUST NOT be issued via multicast addressing.


CC:0033.01.03.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.140: Color Switch Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|
|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|
|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|



**Color** **Component** **ID** **(8** **bits)**

CC:0033.01.03.11.004 This field MUST specify the color component for which the status is requested.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 144




<!-- PAGE 146 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


For the definition of Color Component IDs, refer to section Section 2.2.27.7.


**2.2.27.6** **Color** **Switch** **Report** **Command**


This command is used to advertise the status of a color component.


Table 2.141: Color Switch Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|
|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|
|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|
|Value|Value|Value|Value|Value|Value|Value|Value|



**Color** **Component** **ID** **(8** **bits)**

CC:0033.01.04.11.001 This field MUST advertise the color component covered by this report.

For the definition of Color Component IDs, refer to section Section 2.2.27.7.


**Value** **(8** **bits)**

CC:0033.01.04.11.002 The Value field MUST advertise the value of the color component identified by the Color Component
ID.

CC:0033.01.04.12.001 The Value field SHOULD advertise the current value of the device hardware; also while in transition
to a new target value.


CC:0033.01.04.11.003 A controlling device MUST NOT assume that the Value is identical to a value previously issued with
a Set command; not even when a transition has ended.


**2.2.27.7** **Color** **Switch** **Set** **Command**


This command is used to control one or more color components in a device.


CC:0033.01.05.11.001 Color component levels MUST be scaled by the brightness level. Refer to Section 2.2.27.2


Table 2.142: Color Switch Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|
|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|
|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|
|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|
|…|…|…|…|…|…|…|…|
|Color Component ID N|Color Component ID N|Color Component ID N|Color Component ID N|Color Component ID N|Color Component ID N|Color Component ID N|Color Component ID N|
|Value N|Value N|Value N|Value N|Value N|Value N|Value N|Value N|



**Reserved**

CC:0033.01.05.11.002 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Color** **Component** **Count** **(5** **bits)**


CC:0033.01.05.11.003
This field MUST specify the number of (Color Component ID, Value) datasets contained in the Color
Switch Set command.


**Color** **Component** **ID** **(8** **bits)**

CC:0033.01.05.11.004 This field MUST specify the color component to receive a new value. This field MUST be encoded
according to Table 2.143.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 145




<!-- PAGE 147 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|Component ID|Table 2.143: Color Switch Component IDs Label|Value range|
|---|---|---|
|Component ID|Label|Value range|
|0|Warm White|0x00..0xFF|
|1|Cold White|0x00..0xFF|
|2|Red|0x00..0xFF|
|3|Green|0x00..0xFF|
|4|Blue|0x00..0xFF|
|5|Amber (for 6ch Color mixing)|0x00..0xFF|
|6|Cyan (for 6ch Color mixing)|0x00..0xFF|
|7|Purple (for 6ch Color mixing)|0x00..0xFF|
|8|Indexed Color [OBSOLETED]<br>A supporting node MUST NOT support indexed colors|0x00<br>-<br>0xFF:<br>Color<br>Index<br>0-255|



CC:0033.01.05.11.005 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Value** **(8** **bits)**


CC:0033.01.05.11.006
This field MUST specify the value of the color component identified by the Color Component ID field.


Unlike other actuator control command classes, the Value used by the Color Switch Command Class
CC:0033.01.05.11.007 spans the entire range from 0x00 to 0xFF. Thus, except for the Indexed Color, the value 0x00 MUST
yield to 0% and 0xFF MUST yield to 100% of the actual color component.


**2.2.27.8** **Color** **Switch** **Start** **Level** **Change** **Command**


This command is used to initiate a transition of one color component to a new level.


CC:0033.01.06.11.001
A receiving device MUST initiate the transition to a new value for the specified Color Component ID.


CC:0033.01.06.13.001 The device MAY apply a non-zero duration to the transition from one value to a new value.


Table 2.144: Color Switch Start Level Change Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|
|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|
|Reserved|Up / Down|Ignore Start Level|Reserved|Reserved|Reserved|Reserved|Reserved|
|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|
|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|



**Up/Down** **(1** **bit)**

CC:0033.01.06.11.002 This field MUST specify the direction of the level change.


CC:0033.01.06.11.003 If the Up/Down bit is set to 0 the level change MUST be increasing.


CC:0033.01.06.11.004 If the Up/Down bit is set to 1 the level change MUST be decreasing.


**Ignore** **Start** **Level** **(1** **bit)**


CC:0033.01.06.12.001 A receiving device SHOULD respect the Start Level if the Ignore Start Level bit is 0.


CC:0033.01.06.11.005 A receiving device MUST ignore the Start Level if the Ignore Start Level bit is 1.


CC:0033.01.06.12.002 A controlling device SHOULD set the Ignore Start Level bit to 1.


**Reserved**

CC:0033.01.06.11.006 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 146




<!-- PAGE 148 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Color** **Component** **ID** **(8** **bits)**

CC:0033.01.06.11.007 This field MUST specify the color component to start a transition.

For the definition of Color Component IDs, refer to section Section 2.2.27.7.


**Start** **Level** **(8** **bits)**

CC:0033.01.06.11.008 The Start Level field MUST specify the initial value of the level change.


**2.2.27.9** **Color** **Switch** **Stop** **Level** **Change** **Command**


This command is used to stop an ongoing transition initiated by a Color Switch Start Level Change
Command.

CC:0033.01.07.11.001 A receiving device MUST stop the transition if the specified Color Component ID is currently in
transition to a new value.


CC:0033.01.07.11.002 A receiving device MUST NOT stop ongoing transitions for other Color Component IDs than the one
specified.


Table 2.145: Color Switch Stop Level Change Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|
|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|Command = SWITCH_COLOR_GET|
|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|



**Color** **Component** **ID** **(8** **bits)**

CC:0033.01.07.11.003 This field MUST specify the color component to stop a transition.

For the definition of Color Component IDs, refer to section Section 2.2.27.7.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 147

---

<!-- PAGE 149 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.28** **Color** **Switch** **Command** **Class,** **version** **2**


The Color Switch Command Class, version 2 is used to control color capable devices.


The Color Switch Command Class is an actuator control command class. Refer to Section 2.1.6


**2.2.28.1** **Compatibility** **considerations**


CC:0033.02.00.21.001 A device supporting Color Switch Command Class, version 2 MUST support _Color_ _Switch_ _Command_
_Class,_ _version_ _1_ .


Version 2 adds a duration parameter to the Color Switch Set Command.


Commands not described in this version remain unchanged from version 1.


**2.2.28.1.1** **Command** **Class** **dependencies**


CC:0033.02.00.21.002 Nodes supporting the Color Switch Command Class, version 2 MUST support one of the following
command classes in order to control the color brightness:


      - Multilevel Switch Command Class, version 2


      - Binary Switch Command Class, version 2.


**2.2.28.2** **Interoperability** **considerations**


Refer to Section 2.2.27.2.


**2.2.28.3** **Color** **Switch** **Set** **Command**


This command is used to control one or more color components in a device.


CC:0033.02.05.11.001 Color component levels MUST be scaled by the brightness level. Refer to Section 2.2.27.2.


Table 2.146: Color Switch Set Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|
|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|Command = SWITCH_COLOR_SET|
|_Reserved_|_Reserved_|_Reserved_|Color Component Count|Color Component Count|Color Component Count|Color Component Count|Color Component Count|
|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|
|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|
|…|…|…|…|…|…|…|…|
|Color Component ID N|Color Component ID N|Color Component ID N|Color Component ID N|Color Component ID N|Color Component ID N|Color Component ID N|Color Component ID N|
|Value N|Value N|Value N|Value N|Value N|Value N|Value N|Value N|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|



**Reserved**

CC:0033.02.05.11.002 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Color** **Component** **Count** **(5** **bits)**


CC:0033.02.05.11.003
This field MUST specify the number of (Color Component ID, Value) datasets contained in the Color
Switch Set command.


**Color** **Component** **ID** **(8** **bits)**

CC:0033.02.05.11.004 This field MUST specify the color component to receive a new value.

For the definition of Color Component IDs, refer to section Section 2.2.27.7


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 148




<!-- PAGE 150 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Value** **(8** **bits)**

CC:0033.02.05.11.005 This field MUST specify the value of the color component identified by the Component ID field.


Refer to section Table 2.143.


**Duration** **(8** **bits)**

CC:0033.02.05.11.006 The Duration field MUST specify the time that the transition should take from the current value to
the new target value.

CC:0033.02.05.12.001 A supporting device SHOULD respect the specified Duration value.

CC:0033.02.05.11.007 The encoding of the Duration field MUST be according to Table 2.9.


CC:0033.02.05.12.002 The factory default duration SHOULD be the same as the duration used for the Color Switch Set
command, version 1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 149

---

<!-- PAGE 151 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.29** **Color** **Switch** **Command** **Class,** **version** **3**


The Color Switch Command Class is used to control color capable devices.


The Color Switch Command Class manipulates the color components of a device. Each color component is scaled by the brightness level previously set by a Multilevel Switch Set or Basic Set command.


The Color Switch Command Class is an actuator control command class. Refer to Section 2.1.6.


**2.2.29.1** **Compatibility** **considerations**


CC:0033.03.00.21.001 A node supporting Color Switch Command Class, version 3 MUST support the Color Switch Command Class, version 2.


Version 3 adds duration and target value reporting to the Color Switch Report Command and adds
duration control to the Color Switch Start Level Change Command.


Commands not described in this version remain unchanged from version 2.


CC:0033.03.00.23.001 A node receiving a version 1 Color Switch Set command MAY apply a factory default duration to the

transition.


**2.2.29.1.1** **Command** **Class** **dependencies**


CC:0033.03.00.21.002 Nodes supporting the Color Switch Command Class, version 3 MUST support one of the following
Command Classes in order to control the color brightness:


      - Multilevel Switch Command Class, version 4


      - Binary Switch Command Class, version 2.


**2.2.29.2** **Interoperability** **considerations**


Refer to Section 2.2.28.2


**2.2.29.3** **Color** **Switch** **Report** **Command**


This command is used to advertise the status of a color component.


Table 2.147: Color Switch Report Command, version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|
|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|Command = SWITCH_COLOR_REPORT|
|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|
|Current Value|Current Value|Current Value|Current Value|Current Value|Current Value|Current Value|Current Value|
|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|Target Value|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|



**Color** **Component** **ID** **(8** **bits)**

CC:0033.03.04.11.001 This field MUST advertise the color component covered by this report.


**Current** **Value** **(8** **bits)**

CC:0033.03.04.11.002 The Current Value field MUST advertise the current value of the color component identified by the
Color Component ID.


Refer to the Color Switch Set command for valid values.


CC:0033.03.04.12.001 The Current Value SHOULD be identical to the Target Value when a transition has ended.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 150




<!-- PAGE 152 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Target** **Value** **(8** **bits)**

CC:0033.03.04.11.003 The Target Value field MUST advertise the target value of an ongoing transition or the most recent
transition for the advertised Color Component ID.


Refer to the Color Switch Set command for valid values.


If a transition is initiated in an interactive fashion via a local user interface or via a Start Level Change
CC:0033.03.04.11.004 command, the advertised Target Value MUST be 0x00 or 0xFF, depending on the direction.


CC:0033.03.04.12.002 The Current Value SHOULD be identical to the Target Value when a transition has ended.


**Duration** **(8** **bits)**

CC:0033.03.04.12.003 The Duration field SHOULD advertise the time needed to reach the Target Value at the actual

CC:0033.03.04.11.005 transition rate. The encoding of the Duration field MUST be according to Table 2.10


**2.2.29.4** **Color** **Switch** **Start** **Level** **Change** **Command**


This command is used to initiate a transition of one color component to a new value.


Table 2.148: Color Switch Start Level Change Command, version

|7|Table 2.1 3 6|148: Color Switch Sta 5|art Level C 4|Change Com 3|mmand, ver 2|rsion 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|Command Class = COMMAND_CLASS_SWITCH_COLOR|
|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|Command = SWITCH_COLOR_START_LEVEL_CHANGE|
|Reserved|Up / Down|Ignore Start Level|Reserved|Reserved|Reserved|Reserved|Reserved|
|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|Color Component ID|
|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|



**Up/Down** **(1** **bit)**

CC:0033.03.06.11.001 This field MUST specify the direction of the level change.


CC:0033.03.06.11.002 If the Up/Down bit is set to 0 the level change MUST be increasing.


CC:0033.03.06.11.003 If the Up/Down bit is set to 1 the level change MUST be decreasing.


**Ignore** **Start** **Level** **(1** **bit)**


CC:0033.03.06.12.001 A receiving device SHOULD respect the Start Level if the Ignore Start Level bit is 0.


CC:0033.03.06.11.004 A receiving device MUST ignore the Start Level if the Ignore Start Level bit is 1.


CC:0033.03.06.12.002 A controlling device SHOULD set the Ignore Start Level bit to 1.


**Reserved**

CC:0033.03.06.11.005 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Color** **Component** **ID** **(8** **bits)**


Refer to Color Switch Set command.


**Start** **Level** **(8** **bits)**

CC:0033.03.06.11.006 The Start Level field MUST specify the initial value of the level change.


**Duration** **(8** **bits)**


CC:0033.03.06.11.007 The level change rate MUST be calculated to match a level change from 0x00 to 0xFF during the
time specified by the Duration field.

CC:0033.03.06.12.003 A supporting device SHOULD respect the specified Duration value.


For encoding of the Duration value, refer to the Color Switch Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 151