<!-- PAGE 624 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.11** **Battery** **Command** **Class,** **version** **1**


The Battery Command Class is used to request and report battery levels for a given device.


**3.2.11.1** **Battery** **Get** **Command**


The Battery Get Command is used to request the level of a battery.


CC:0080.01.02.11.001 The _Battery_ _Report_ _Command_ MUST be returned in response to this command.


CC:0080.01.02.11.002 This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.38: Battery Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|
|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|



**3.2.11.2** **Battery** **Report** **Command**


This command is used to report the battery level of a battery operated device.


Table 3.39: Battery Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|
|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|
|Battery Level|Battery Level|Battery Level|Battery Level|Battery Level|Battery Level|Battery Level|Battery Level|



**Battery** **Level** **(8** **bits)**

This field is used to report the percentage indicating the battery level.

CC:0080.01.03.11.001 This field MUST be in the range 0x00..0x64 or set to 0xFF.


CC:0080.01.03.11.002 Values in the range 0x00..0x64 MUST indicate the battery percentage level from 0 to 100%.


CC:0080.01.03.11.003 The value 0xFF MUST indicate a low-battery warning which MUST only be sent unsolicited. When
a controller requests the battery level using a BATTERY_GET command, the actual battery level
(0-100) MUST be returned. Recommendation is to send the low-battery value (0xFF) when the device
battery level indicates the battery should be replaced or recharged within a few days or weeks. The
low-battery warning SHOULD be sent no more than once per day. The device manufacturer knows the
chemistry and discharge characteristics of the battery but the controller does not. Thus the controller
cannot use a simple battery percentage threshold to decide when to inform the user the battery need
to be replaced. For example, the device manufacturer may choose a battery level of 20% for the
low-battery warning point for a lithium battery which has a steep discharge curve at end-of-life or 5%
for alkaline cells which has a more linear discharge curve. The point where the low-battery warning
is sent is at the discretion of the device manufacturer. Controllers SHOULD inform the user that the
battery needs replacement or recharging each time the low-battery warning (0xFF) is received.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 623

---

<!-- PAGE 625 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.12** **Battery** **Command** **Class,** **version** **2**


This Command Class is used to request and report the battery types, status and levels of a given
device.


**3.2.12.1** **Compatibility** **Considerations**


The following commands has been extended to query status and levels of a battery:


 - _Battery_ _Get_ _Command_


 - _Battery_ _Report_ _Command_


The following commands are added for requesting the current health of the battery.


 - _Battery_ _Health_ _Get_ _Command_


 - _Battery_ _Health_ _Report_ _Command_


**3.2.12.2** **Battery** **Get** **Command**


This command is used to request both the level of a battery and its status.


The _Battery_ _Report_ _Command_ MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.40: Battery Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|
|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|Command = BATTERY_GET (0x02)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 624




<!-- PAGE 626 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.12.3** **Battery** **Report** **Command**


This command is used to report the level and status of a battery-operated device.


Table 3.41: Battery Level Report Command














|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|
|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|
|Battery Level|Battery Level|Battery Level|Battery Level|Battery Level|Battery Level|Battery Level|Battery Level|
|Battery Charging<br>Status|Battery Charging<br>Status|Recharge-<br>able|Back-up<br>battery|Over-<br>heating|Low<br>fuid|Replace/recharge status<br>bitmask|Replace/recharge status<br>bitmask|
||||||||Discon-<br>nected|



**Battery** **Level** **(8** **bits)**

This field is used to report the percentage indicating the battery level. This field MUST be in the
range 0x00..0x64 or set to 0xFF. Values in the range 0x00..0x64 MUST indicate the battery percentage
level from 0 to 100%.

The value 0xFF MUST indicate a low-battery warning and this notification MUST only be sent as
an unsolicited Report to the Lifeline destinations. When a controller requests the battery level, the
actual battery level (0-100) MUST be returned. The percentage level of 0% represents the lowest
operational voltage of the device. For example; if the device can no longer operate properly below a
battery voltage of 2.2V, the device should report 0% level when the battery voltage reaches 2.2V.


Recommendation is to send the low-battery value (0xFF) when the device battery level indicates
the battery should be replaced or recharged within a few days or weeks. The low-battery warning
SHOULD be sent no more than once per day. The device manufacturer knows the chemistry and
discharge characteristics of the battery but the controller does not. Thus the device chooses when the
user should be informed of the low battery condition. The device manufacturer may choose a battery
level of 20% for the low-battery warning point for a lithium battery which has a steep discharge curve
at end-of-life or 5% for alkaline cells which has a more linear discharge curve. The point where the
low-battery warning is sent is at the discretion of the device manufacturer. Controllers SHOULD
inform the user that the battery needs replacement each time the low-battery warning (0xFF) is
received.

The Replace/Recharge field MUST have at least bit 0 set when the low-battery warning is sent.


**Battery** **Charging** **Status** **(2** **bits)**

CC:0080.02.03.11.001 The field describes the charging status of a battery if the _Rechargeable_ flag field is 1. The field MUST
be encoded according to Table 3.42.

CC:0080.02.03.11.002 If the _Rechargeable_ flag field is set to 0, the battery charging status value MUST be 0x00.


Table 3.42: Charging status notification values: Battery Command

|Table 3.42: Chargi Class Value|ing status notification values: Battery Command Description|
|---|---|
|Value|Description|
|0x00|Discharging|
|0x01|Charging|
|0x02|Maintaining|



**Rechargeable** **(1** **bit)**

This field indicates if the battery is rechargeable or not.

CC:0080.02.03.11.003 If the battery is rechargeable this field MUST be set to 1.

CC:0080.02.03.11.004 If the battery is not rechargeable, the field value MUST set to 0.


**Back-up** **battery** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 625




<!-- PAGE 627 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to illustrate if the battery is utilized for back-up purposes of a mains powered
connected device.

CC:0080.02.03.11.005 If the battery is used for back-up purposes the field MUST be set to 1.

CC:0080.02.03.11.006 If battery is the primary means of power and is not for back-up, this field MUST set to 0.


**Overheating** **(1** **bit)**

This field is used to indicate if overheating is detected at the battery.


CC:0080.02.03.11.007 The value 1 MUST indicate that the battery is overheating


CC:0080.02.03.11.008 The value 0 MUST indicate that the battery is operating within the normal temperature range.

**Low** **fluid** **(1** **bit)**

This field is used to indicate if the battery fluid is low and should be refilled.

CC:0080.02.03.11.009 The value 1 MUST indicate that the battery fluid is low.

CC:0080.02.03.11.00A The value 0 MUST indicate that the battery fluid is within the normal range and no maintenance is
required.


**Replace/recharge** **status** **bitmask** **(2** **bits)**

This field is used to indicate if the battery needs to be recharged or replaced.


CC:0080.02.03.11.00B Bit 0 set to 1 MUST indicate that the battery MUST be replaced/recharged soon.


CC:0080.02.03.11.00C Bit 1 set to 1 MUST indicate that the battery MUST be replaced/recharged now.


CC:0080.02.03.11.00D If bit 1 is set to 1, bit 0 MUST also be set to 1.


**Disconnected** **(1** **bit)**

This field is used to indicate if the battery is currently disconnected or removed from the node.


CC:0080.02.03.11.00E The value 1 MUST indicate that the battery is disconnected and the node is running on an alternative

power source.


CC:0080.02.03.11.00F The value 0 MUST indicate that the battery correctly connected to the node.

CC:0080.02.03.11.010 If this field is set to 1, the _Battery_ _Level_ field MUST be set to 0x00.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 626




<!-- PAGE 628 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.12.4** **Battery** **Health** **Get** **Command**


This command is used to query the health of the battery, particularly the battery temperature and
maximum capacity.


CC:0080.02.04.11.001 The _Battery_ _Health_ _Report_ _Command_ MUST be returned in response to this command.


CC:0080.02.04.11.002 This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.43: Battery Health Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|
|Command = BATTERY_HEALTH_GET (0x04)|Command = BATTERY_HEALTH_GET (0x04)|Command = BATTERY_HEALTH_GET (0x04)|Command = BATTERY_HEALTH_GET (0x04)|Command = BATTERY_HEALTH_GET (0x04)|Command = BATTERY_HEALTH_GET (0x04)|Command = BATTERY_HEALTH_GET (0x04)|Command = BATTERY_HEALTH_GET (0x04)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 627




<!-- PAGE 629 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.12.5** **Battery** **Health** **Report** **Command**


This command is used to report the maximum capacity of the battery as well as the temperature of
the battery.


Table 3.44: Battery Health Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|
|Command = BATTERY_HEALTH_REPORT (0x05)|Command = BATTERY_HEALTH_REPORT (0x05)|Command = BATTERY_HEALTH_REPORT (0x05)|Command = BATTERY_HEALTH_REPORT (0x05)|Command = BATTERY_HEALTH_REPORT (0x05)|Command = BATTERY_HEALTH_REPORT (0x05)|Command = BATTERY_HEALTH_REPORT (0x05)|Command = BATTERY_HEALTH_REPORT (0x05)|
|Maximum Capacity|Maximum Capacity|Maximum Capacity|Maximum Capacity|Maximum Capacity|Maximum Capacity|Maximum Capacity|Maximum Capacity|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Battery Temperature 1|Battery Temperature 1|Battery Temperature 1|Battery Temperature 1|Battery Temperature 1|Battery Temperature 1|Battery Temperature 1|Battery Temperature 1|
|…|…|…|…|…|…|…|…|
|Battery Temperature N|Battery Temperature N|Battery Temperature N|Battery Temperature N|Battery Temperature N|Battery Temperature N|Battery Temperature N|Battery Temperature N|



**Maximum** **Capacity** **(8** **bits)**

This field is used to report the percentage indicating the maximum capacity of the battery.

CC:0080.02.05.11.001 This field MUST be in the range 0x00..0x64 or set to 0xFF. If the maximum capacity of the battery
is unknown the value MUST set to 0xFF.


CC:0080.02.05.11.002 Values in the range 0x00..0x64 MUST indicate the maximum capacity of the battery in the percentage
level from 0 to 100%.


For example, if the initial battery total capacity is 1500mAh, 100% represents this value. If subsequently the node detects that the total battery capacity when fully loaded is down to 1350, it must
report 90%.


**Precision** **(3** **bits)**

This field is used to indicate how many decimal places are included in the _Battery_ _Temperature_ field.
For example, the _Battery_ _Temperature_ field set to 1025 with the Precision field set to 2 MUST be
interpreted as 10.25.


**Scale** **(2** **bits)**


CC:0080.02.05.11.003
The scale field indicates the scale used for the battery temperature value. This field MUST be encoded
according to Table 10


Table 3.45: Battery Health Report: Scale field encoding

|Value|Description|
|---|---|
|0x00|Celsius|
|0x01..0x03|Reserved|



**Size** **(3** **bits)**

CC:0080.02.05.11.004 The size field indicates the number of bytes used for the battery temperature value. This field MUST
be set to 0, 1, 2 or 4.


CC:0080.02.05.11.005 The value 0 MUST indicate that the battery temperature is unknown. In this case, the _Scale_ and

CC:0080.02.05.11.006 _Precision_ fields MUST be set to 0 and the _Battery_ _Temperature_ field MUST be omitted.

CC:0080.02.05.11.007 Values 1, 2 and 4 MUST indicate the length in bytes of the _Battery_ _Temperature_ field.


**Battery** **Temperature** **(N** **bytes)**

This field advertises the temperature of the battery.

CC:0080.02.05.11.008 The length of this field in bytes MUST be according to the Size field.

CC:0080.02.05.11.009 The first byte MUST be the most significant byte.

CC:0080.02.05.11.010 This field MUST be encoded using signed representation and comply with Signed field encoding
representation (Table 2.12).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 628

---

<!-- PAGE 630 -->

CC:0080.03.00.21.001



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.13** **Battery** **Command** **Class,** **version** **3**


This Command Class is used to request and report the battery types, status and levels of a given
device. The Battery Command Class, version 3 is backwards compatible with the Battery Command
Class, version 2. Fields and commands not described in this version MUST remain unchanged from
version 2.


The Battery Report Command has been extended to advertise if the device battery is stop charging
due to low temperature.


**3.2.13.1** **Battery** **Report** **Command**


This command is used to report the level and status of battery-operated device


Table 3.46: Battery Report Command, version 3
















|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|Command Class = COMMAND_CLASS_BATTERY (0x80)|
|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|Command = BATTERY_REPORT (0x03)|
|Battery Level|Battery Level|Battery Level|Battery Level|Battery Level|Battery Level|Battery Level|Battery Level|
|Battery Charging<br>Status|Battery Charging<br>Status|Rechar<br>geable|Back-up<br>Battery|Overhe<br>ating|Low<br>Fluid|Replace/recharge status bit-<br>mask|Replace/recharge status bit-<br>mask|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Low Tem<br>perature Status|Discon<br>nected|



All fields not described below remain unchanged from version 2.


**Low** **Temperature** **Status** **(1** **bit)**


This status is used to advertise if the battery of a device has stopped charging due to low temperature.


CC:0080.03.03.11.001 The value 1 MUST indicate that the battery is not charging due to low temperature.


The value 0 MUST indicate that the battery is operational.

CC:0080.03.03.11.002 If the battery is not rechargeable, the field value MUST set to 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 629