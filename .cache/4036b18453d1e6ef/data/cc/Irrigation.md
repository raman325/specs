<!-- PAGE 261 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.51** **Irrigation** **Command** **Class,** **version** **1**


The Irrigation Command Class provides commands to manage irrigation systems.


**2.2.51.1** **Terminology**


In an irrigation system, a **zone** **valve** is turned on to allow a certain group of sprinklers to water an
area (or **zone** ) for a specified duration. The terms **zone** **valve** and **valve** are used synonymously,
whereas a **main** **valve** is always identified as such.


A valve that is **on** or **open** lets the water run through the valve.

A valve that is **off** or **closed** blocks the water from running through the valve.

A **main** **valve** allows water to flow to a set of zone valves, and must be turned on before water flows
to the zone valves. In version 1 of this Command Class, there is only one main valve in an irrigation
system.

A valve is identified with a **ValveID** . The main valve and zone valves have their own ID pools, each
starting with 1.


In some cases a main valve switch may drive a pump relay rather than an actual irrigation valve. In
this case, there may be a configurable delay between the main valve (or pump) being turned on and
the rest of the zone valves being turned on. When a given zone is turned on, a main valve (if present)
should automatically turn on. The main valve should also automatically turn off after a device specific
duration of zone valve inactivity.


A valve can be physically **connected** or **disconnected** . Attach points where valves can be connected
always keep the same valve ID. A disconnected valve cannot be operated and the water does not run
through a disconnected valve.


In an irrigation system, a **scheduled** **run** or **run** is when a set of zone valves are open and closed
sequentially, one after another. Each zone valve will be turned on for a specified duration and once
complete, that valve will be turned off and the next zone valve will be turned on. In a (scheduled)
run, each zone valve has its own specified run duration, which is unique to that zone valve and that
specific (scheduled) run. At the end of a scheduled run, the Irrigation System Shutoff Command can
also be used to turn everything off.


A main valve remains on/open for the entire duration of any run, so that all zone valves will be able
to provide water to their associated sprinklers.


A **valve** **table** is a list of zone valves and their corresponding run durations. A valve table can be
created, configured and stored in an irrigation device. The valve table can subsequently be executed
(or run) using a single command.


**2.2.51.2** **Compatibility** **considerations**


**2.2.51.2.1** **Multi** **Channel** **considerations**


CC:006B.01.00.22.001 Multi Channel End Points SHOULD NOT support the Irrigation Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 260




<!-- PAGE 262 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.51.3** **Interoperability** **considerations**


CC:006B.01.00.32.001 A node supporting the Irrigation Command Class SHOULD be implemented as a Multi Channel
Device with the main valve and each zone valve implemented as a separate Multi Channel End Point.


CC:006B.01.00.32.002 The Root Device SHOULD support the following Command Classes:


      - Irrigation Command Class


      - Schedule Command Class


CC:006B.01.00.32.003 Each End Point SHOULD support the following Command Class:


      - Binary Switch Command Class


CC:006B.01.00.32.004 A node supporting optional sensors SHOULD implement each sensor as a separate Multi Channel
End Point.

The Notification Command Class, version 7 or newer can be used for reporting Irrigation events/states,
using the Irrigation Notification Type.


Scheduling can be done using the Schedule Command Class. If supported, the Schedule Command
CC:006B.01.00.32.005 Class SHOULD support alternating days and odd/even date processing.


CC:006B.01.00.33.001 Some supporting nodes MAY support having only 1 zone valve open at a time. A controlling node

CC:006B.01.00.32.006 SHOULD be aware that opening a zone valve may cause another currently open zone valve to close.


**2.2.51.3.1** **Controlling** **methods**


A system integrator should be aware that if an irrigation control device is controlled using both
End Point Binary Switch Command Class and Root Device Irrigation Command Class at the same
time, this may cause unpredictable behavior. This applies whether commands are issued instantly or
scheduled.


CC:006B.01.00.32.007 It is RECOMMENDED that an irrigation controlling system is managed either via direct End Point
control or via the Irrigation Command Class.


An irrigation device can be driven directly from a Z-Wave controlling node, turning on the main valve
and sequentially turning on each zone valve for a specified duration.


The controlling node can also use the concept of a valve table to turn on a set of valves sequentially. A
valve table allows a single command, the Irrigation Valve Table Run Command, to trigger a run. The
controlling node must first create the valve tables, using the Irrigation Valve Table Set Command.
The run can triggered by sending the Irrigation Valve Table Run Command at the desired time. The
irrigation device will sequentially run the valves in each of the specified valve tables for their associated
runtimes. Depending on the irrigation system, the controlling node may need to turn on the main
valve manually using the Irrigation Valve Run Command.


**2.2.51.4** **Irrigation** **System** **Info** **Get** **Command**


This command is used to request a receiving node about its irrigation system information.


CC:006B.01.01.11.001 The Irrigation System Info Report Command MUST be returned in response to this command.


CC:006B.01.01.11.002 This command MUST NOT be issued via multicast addressing.


CC:006B.01.01.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.307: Irrigation System Info Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_SYSTEM_INFO_GET|Command = IRRIGATION_SYSTEM_INFO_GET|Command = IRRIGATION_SYSTEM_INFO_GET|Command = IRRIGATION_SYSTEM_INFO_GET|Command = IRRIGATION_SYSTEM_INFO_GET|Command = IRRIGATION_SYSTEM_INFO_GET|Command = IRRIGATION_SYSTEM_INFO_GET|Command = IRRIGATION_SYSTEM_INFO_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 261




<!-- PAGE 263 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.51.5** **Irrigation** **System** **Info** **Report** **Command**


This command is used to advertise irrigation system information.


Table 2.308: Irrigation System Info Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_SYSTEM_INFO_REPORT|Command = IRRIGATION_SYSTEM_INFO_REPORT|Command = IRRIGATION_SYSTEM_INFO_REPORT|Command = IRRIGATION_SYSTEM_INFO_REPORT|Command = IRRIGATION_SYSTEM_INFO_REPORT|Command = IRRIGATION_SYSTEM_INFO_REPORT|Command = IRRIGATION_SYSTEM_INFO_REPORT|Command = IRRIGATION_SYSTEM_INFO_REPORT|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Main Valve|
|Total Number of Valves|Total Number of Valves|Total Number of Valves|Total Number of Valves|Total Number of Valves|Total Number of Valves|Total Number of Valves|Total Number of Valves|
|Total Number of Valve Tables|Total Number of Valve Tables|Total Number of Valve Tables|Total Number of Valve Tables|Total Number of Valve Tables|Total Number of Valve Tables|Total Number of Valve Tables|Total Number of Valve Tables|
|Reserved|Reserved|Reserved|Reserved|Valve Table Max Size|Valve Table Max Size|Valve Table Max Size|Valve Table Max Size|



**Reserved**

CC:006B.01.02.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Main** **Valve** **(1** **bit)**

This field is used to indicate if a main valve is supported by the sending node.


CC:006B.01.02.11.002 The value 1 MUST indicate that the sending node supports a main valve.


CC:006B.01.02.11.003 The value 0 MUST indicate that the sending node does not support a main valve.


**Total** **Number** **of** **Valves** **(8** **bits)**

This field is used to advertise the total number of zone valves supported by the device


CC:006B.01.02.11.004 The implemented Valve ID values MUST be in a sequence starting from 1, i.e. a node supporting 10
valves MUST accept Valve ID values in the range 1..10.


**Total** **Number** **of** **Valve** **Tables** **(8** **bits)**

This field is used to advertise the total number of valve tables that can be created/stored in the device.


CC:006B.01.02.11.005 The implemented Valve Table ID MUST be in a sequence starting from 1, i.e. a node supporting 10
valve tables MUST accept Valve Table ID values in the range 1..10.


**Valve** **Table** **Max** **Size** **(4** **bits)**

This field is used to advertise the maximum number of entries per valve table supported by the sending
node.


CC:006B.01.02.11.006 The value MUST be in the range 1..15.


**2.2.51.6** **Irrigation** **System** **Status** **Get** **Command**


This command is used to request a receiving node about its irrigation system status.


CC:006B.01.03.11.001 The Irrigation System Status Report Command MUST be returned in response to this command.


CC:006B.01.03.11.002 This command MUST NOT be issued via multicast addressing.


CC:006B.01.03.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.309: Irrigation System Status Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_SYSTEM_STATUS_GET|Command = IRRIGATION_SYSTEM_STATUS_GET|Command = IRRIGATION_SYSTEM_STATUS_GET|Command = IRRIGATION_SYSTEM_STATUS_GET|Command = IRRIGATION_SYSTEM_STATUS_GET|Command = IRRIGATION_SYSTEM_STATUS_GET|Command = IRRIGATION_SYSTEM_STATUS_GET|Command = IRRIGATION_SYSTEM_STATUS_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 262




<!-- PAGE 264 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.51.7** **Irrigation** **System** **Status** **Report** **Command**


This command is used to advertise irrigation system status.


Table 2.310: Irrigation System Status Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_SYSTEM_STATUS_REPORT|Command = IRRIGATION_SYSTEM_STATUS_REPORT|Command = IRRIGATION_SYSTEM_STATUS_REPORT|Command = IRRIGATION_SYSTEM_STATUS_REPORT|Command = IRRIGATION_SYSTEM_STATUS_REPORT|Command = IRRIGATION_SYSTEM_STATUS_REPORT|Command = IRRIGATION_SYSTEM_STATUS_REPORT|Command = IRRIGATION_SYSTEM_STATUS_REPORT|
|System Voltage|System Voltage|System Voltage|System Voltage|System Voltage|System Voltage|System Voltage|System Voltage|
|Sensor Status|Sensor Status|Sensor Status|Sensor Status|Sensor Status|Sensor Status|Sensor Status|Sensor Status|
|Flow Precision|Flow Precision|Flow Precision|Flow Scale=l/h|Flow Scale=l/h|Flow Size|Flow Size|Flow Size|
|Flow Value 1|Flow Value 1|Flow Value 1|Flow Value 1|Flow Value 1|Flow Value 1|Flow Value 1|Flow Value 1|
|…|…|…|…|…|…|…|…|
|Flow Value N|Flow Value N|Flow Value N|Flow Value N|Flow Value N|Flow Value N|Flow Value N|Flow Value N|
|Pressure Precision|Pressure Precision|Pressure Precision|Pressure Scale=kPa|Pressure Scale=kPa|Pressure Size|Pressure Size|Pressure Size|
|Pressure Value 1|Pressure Value 1|Pressure Value 1|Pressure Value 1|Pressure Value 1|Pressure Value 1|Pressure Value 1|Pressure Value 1|
|…|…|…|…|…|…|…|…|
|Pressure Value N<br>|Pressure Value N<br>|Pressure Value N<br>|Pressure Value N<br>|Pressure Value N<br>|Pressure Value N<br>|Pressure Value N<br>|Pressure Value N<br>|
|Shutof Duration|Shutof Duration|Shutof Duration|Shutof Duration|Shutof Duration|Shutof Duration|Shutof Duration|Shutof Duration|
|System Error Status|System Error Status|System Error Status|System Error Status|System Error Status|System Error Status|System Error Status|System Error Status|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Main Valve|
|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|



**System** **Voltage** **(8** **bits)**

This field advertises the voltage level applied at the sending node.

CC:006B.01.04.11.001 The advertised value MUST be expressed in Volt. This field does not indicate the voltage type (AC
or DC).

CC:006B.01.04.11.002 If the node does not have a voltage sensor measuring the voltage, this field MUST be set to 0.


**Sensor** **Status** **(8** **bits)**

This field is used to advertise if optional sensors are currently reporting values or detecting events at
the sending node.

CC:006B.01.04.11.003 This field MUST be treated as a bit mask and MUST comply with Table 2.311

|Bit|Table 2.311: Irrigation System Status Report::Sensor Status en- coding Sensor Status|
|---|---|
|Bit|Sensor Status|
|0|Flow Sensor currently active<br>If this bit is set to 1, the Flow Value feld value MUST advertise a valid sensor reading.|
|1|Pressure Sensor currently active<br>If this bit is set to 1, the Pressure Value feld value MUST advertise a valid sensor reading.|
|2|Rain Sensor attached and active<br>If a rain sensor is currently attached to the device and detecting rain, this bit MUST be<br>set to 1.|
|3|Moisture Sensor attached and active<br>If a moisture sensor is currently attached to the device and detecting moisture, this bit<br>MUST be set to 1.|
|4..7|_Reserved_|



CC:006B.01.04.11.004 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Flow** **Precision** **(3** **bits)**


CC:006B.01.04.11.005


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 263




<!-- PAGE 265 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST indicate how many decimals are contained in the “Flow Value” field value. For
example, if the “Flow Value” field is set to 1025 and the “Flow Precision” field is set to 2, the Flow
Value MUST be interpreted as 10.25.

CC:006B.01.04.11.006 If the Sensor Status field’s bit 0 is set to 0, this field MUST be set to 0.


**Flow** **Scale** **(2** **bits)**

CC:006B.01.04.11.007 This field MUST indicate which unit is used for the “Flow Value” field. This field MUST be set to 0.


CC:006B.01.04.11.008 The value 0 MUST indicate that the unit is l/h (liter/hour)


**Flow** **Size** **(3** **bits)**

CC:006B.01.04.11.009 This field is used to advertise the length in bytes of the “Flow Value” field. This field MUST be set
to 1, 2 or 4. All other values are reserved and MUST NOT be used by a sending node.

CC:006B.01.04.11.00A If the Sensor Status field’s bit 0 is set to 0, this field MUST be set to 1.


**Flow** **Value** **(N** **bytes)**

This field is used to advertise the Flow value measured by the flow sensor.

CC:006B.01.04.11.00B The length of this field in byte MUST comply with the value advertised in the Flow Size field.

CC:006B.01.04.11.00C If the Sensor Status field’s bit 0 is set to 0, this field MUST be set to 0 by a sending node and MUST
be ignored by a receiving node.


**Pressure** **Precision** **(3** **bits)**

CC:006B.01.04.11.00D This field MUST indicate how many decimals are contained in the “Pressure Value” field value. For
example, if the “Pressure Value” field is set to 1025 and the “Pressure Precision” field is set to 2, the
Pressure Value MUST be interpreted as 10.25.

CC:006B.01.04.11.00E If the Sensor Status field’s bit 1 is set to 0, this field MUST be set to 0.


**Pressure** **Scale** **(2** **bits)**

CC:006B.01.04.11.00F This field MUST indicate which unit is used for the “Pressure Value” field. This field MUST be set
to 0.


CC:006B.01.04.11.010 The value 0 MUST indicate that the unit is kPa (kilopascal)


**Pressure** **Size** **(3** **bits)**

CC:006B.01.04.11.011 This field is used to advertise the length in bytes of the “Pressure Value” field. This field MUST be
set to 1, 2 or 4. All other values are reserved and MUST NOT be used by a sending node.

CC:006B.01.04.11.012 If the Sensor Status field’s bit 1 is set to 0, this field MUST be set to 1.


**Pressure** **Value** **(N** **bytes)**

This field is used to advertise the Pressure value measured by the pressure sensor.

CC:006B.01.04.11.013 The length of this field in bytes MUST comply with the value advertised in the Pressure Size field.

CC:006B.01.04.11.014 If the Sensor Status field’s bit 1 is set to 0, this field MUST be set to 0 by a sending node and MUST
be ignored by a receiving node.

**Shutoff** **Duration** **(8** **bits)**

This field is used to indicate how many hours are left in the “shut off” mode.

For description, refer to Irrigation System Shutoff Command (Section 2.2.51.21).


**System** **Error** **Status** **(8** **bits)**

This field is used to advertise if any system error is being active at the sending node.

CC:006B.01.04.11.015 This field MUST be treated as a bit mask and MUST comply with Table 2.312.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 264




<!-- PAGE 266 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|Bit|Table 2.312: System Status Report::System Error Status encoding Description|
|---|---|
|Bit|Description|
|0|The device has not been programmed|
|1|The device has experienced an emergency shutdown.|
|2|The device’s pressure high threshold has been triggered.|
|3|The device’s pressure low threshold has been triggered.|
|4|A valve or the main valve is reporting error.<br>Valves can be individually checked using the Irrigation Valve Info Get Command|
|5..7|_Reserved_|



In some cases, errors are no longer active. Any inactive errors (except valve errors) can be cleared
by sending an Irrigation System Config Set Command. Refer to the Irrigation Valve Info Report
Command for more details on valve specific errors.


**Main** **Valve** **(1** **bit)**

This field is used to indicate if a main valve is currently open or closed.


CC:006B.01.04.11.016 The value 1 MUST indicate that the main valve is On / Open.

CC:006B.01.04.11.017 The value 0 MUST indicate that the main valve is Off / Closed.


**Valve** **ID** **(8** **bits)**

This field is used to indicate the Valve ID of the first open zone valve currently On / Open.

CC:006B.01.04.11.018 If no zone valve is On / Open, this field MUST be set to 0.

CC:006B.01.04.11.019 Else, this field MUST be to a value in the range 1..{Total number of supported zone valves} by a
sending node


**2.2.51.8** **Irrigation** **System** **Config** **Set** **Command**


This command allows the irrigation system to be configured accordingly.


Table 2.313: Irrigation System Config Set Command













|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_SYSTEM_CONFIG_SET|Command = IRRIGATION_SYSTEM_CONFIG_SET|Command = IRRIGATION_SYSTEM_CONFIG_SET|Command = IRRIGATION_SYSTEM_CONFIG_SET|Command = IRRIGATION_SYSTEM_CONFIG_SET|Command = IRRIGATION_SYSTEM_CONFIG_SET|Command = IRRIGATION_SYSTEM_CONFIG_SET|Command = IRRIGATION_SYSTEM_CONFIG_SET|
|Main Valve Delay|Main Valve Delay|Main Valve Delay|Main Valve Delay|Main Valve Delay|Main Valve Delay|Main Valve Delay|Main Valve Delay|
|High Pressure Threshold Preci-<br>sion|High Pressure Threshold Preci-<br>sion|High Pressure Threshold Preci-<br>sion|High Pressure Threshold<br>Scale=kPa|High Pressure Threshold<br>Scale=kPa|High Pressure Threshold<br>Size|High Pressure Threshold<br>Size|High Pressure Threshold<br>Size|
|High Pressure Threshold Value 1|High Pressure Threshold Value 1|High Pressure Threshold Value 1|High Pressure Threshold Value 1|High Pressure Threshold Value 1|High Pressure Threshold Value 1|High Pressure Threshold Value 1|High Pressure Threshold Value 1|
|…|…|…|…|…|…|…|…|
|High Pressure Threshold Value N|High Pressure Threshold Value N|High Pressure Threshold Value N|High Pressure Threshold Value N|High Pressure Threshold Value N|High Pressure Threshold Value N|High Pressure Threshold Value N|High Pressure Threshold Value N|
|Low Pressure Threshold Preci-<br>sion|Low Pressure Threshold Preci-<br>sion|Low Pressure Threshold Preci-<br>sion|Low Pressure Threshold<br>Scale=kPa|Low Pressure Threshold<br>Scale=kPa|Low Pressure Threshold Size|Low Pressure Threshold Size|Low Pressure Threshold Size|
|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|
|…|…|…|…|…|…|…|…|
|Low Pressure Threshold Value N|Low Pressure Threshold Value N|Low Pressure Threshold Value N|Low Pressure Threshold Value N|Low Pressure Threshold Value N|Low Pressure Threshold Value N|Low Pressure Threshold Value N|Low Pressure Threshold Value N|
|Sensor Polarity|Sensor Polarity|Sensor Polarity|Sensor Polarity|Sensor Polarity|Sensor Polarity|Sensor Polarity|Sensor Polarity|


**Main** **Valve** **Delay** **(8** **bits)**

This field is used to configure a delay in seconds between turning on the mainvalve and turning on
any “zone” valve.

CC:006B.01.05.11.001 This field MUST ignored by a receiving node if it does not implement a main valve.


CC:006B.01.05.11.002 The value MUST be expressed in seconds and the value 0 MUST indicate that no delay is applied
when turning main and zone valves on.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 265




<!-- PAGE 267 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Pressure** **High** **Threshold**

These fields are used to configure the pressure high threshold at the receiving node.

CC:006B.01.05.13.001 A receiving node having no support for pressure sensor MAY ignore this field.


CC:006B.01.05.11.003 If the receiving node supports a Pressure Sensor, the node MUST issue an Irrigation System Status
Report Command with the System Error Status indicating high pressure when the pressure crosses
above this threshold.


CC:006B.01.05.11.004
The format of the Pressure High Threshold fields MUST comply with the format used by the Multilevel
Sensor Command Class and MUST be expressed in kPa.


**Pressure** **Low** **Threshold**

These fields are used to configure the pressure low threshold at the receiving node.

CC:006B.01.05.13.002 A receiving node having no support for pressure sensor MAY ignore this field.


CC:006B.01.05.11.005 If the receiving node supports a Pressure Sensor, the node MUST issue an Irrigation System Status
Report Command with the System Error Status indicating low pressure when the pressure crosses
below this threshold.


CC:006B.01.05.11.006
The format of the Pressure Low Threshold fields MUST comply with the format used by the Multilevel
Sensor Command Class and MUST be expressed in kPa.


**Sensor** **Polarity** **(8** **bits)**

This field is used to configure optional sensors’ polarity at the receiving node.

CC:006B.01.05.11.007 This field MUST be treated as a bit mask and MUST comply with Table 2.314. This field MUST be
ignored if the ‘valid’ bit (bit 7) is set to 0.


Table 2.314: Irrigation System Config Set::Sensor Polarity encod
|Table 2. ing Bit|.314: Irrigation System Config Set::Sensor Polarity encod- Description|
|---|---|
|Bit|Description|
|0|Rain Sensor Polarity (0 LOW, 1 HIGH)<br>A receiving node having no support for rain sensor MAY ignore this feld.|
|1|Moisture Sensor Polarity (0 LOW, 1 HIGH)<br>A receiving node having no support for moisture sensor MAY ignore this<br>feld|
|2..6|_Reserved_|
|7|Valid<br>This bit MUST be set to 1 to indicate that the other bits in the bitmask<br>contain valid data.|



CC:006B.01.05.11.008 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**2.2.51.9** **Irrigation** **System** **Config** **Get** **Command**


This command is used to request a receiving node about its current irrigation system configuration.

CC:006B.01.06.11.001 The Irrigation System Config Report Command MUST be returned in response to this command.


CC:006B.01.06.11.002 This command MUST NOT be issued via multicast addressing.


CC:006B.01.06.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.315: Irrigation System Config Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_SYSTEM_CONFIG_GET|Command = IRRIGATION_SYSTEM_CONFIG_GET|Command = IRRIGATION_SYSTEM_CONFIG_GET|Command = IRRIGATION_SYSTEM_CONFIG_GET|Command = IRRIGATION_SYSTEM_CONFIG_GET|Command = IRRIGATION_SYSTEM_CONFIG_GET|Command = IRRIGATION_SYSTEM_CONFIG_GET|Command = IRRIGATION_SYSTEM_CONFIG_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 266




<!-- PAGE 268 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.51.10** **Irrigation** **System** **Config** **Report** **Command**


This command is used to advertise the current irrigation system configuration.


Table 2.316: Irrigation System Config Report Command













|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_SYSTEM_CONFIG_REPORT|Command = IRRIGATION_SYSTEM_CONFIG_REPORT|Command = IRRIGATION_SYSTEM_CONFIG_REPORT|Command = IRRIGATION_SYSTEM_CONFIG_REPORT|Command = IRRIGATION_SYSTEM_CONFIG_REPORT|Command = IRRIGATION_SYSTEM_CONFIG_REPORT|Command = IRRIGATION_SYSTEM_CONFIG_REPORT|Command = IRRIGATION_SYSTEM_CONFIG_REPORT|
|Main Valve Delay|Main Valve Delay|Main Valve Delay|Main Valve Delay|Main Valve Delay|Main Valve Delay|Main Valve Delay|Main Valve Delay|
|High Pressure Threshold Preci-<br>sion|High Pressure Threshold Preci-<br>sion|High Pressure Threshold Preci-<br>sion|High Pressure Threshold<br>Scale=kPa|High Pressure Threshold<br>Scale=kPa|High Pressure Threshold<br>Size|High Pressure Threshold<br>Size|High Pressure Threshold<br>Size|
|High Pressure Threshold Value 1|High Pressure Threshold Value 1|High Pressure Threshold Value 1|High Pressure Threshold Value 1|High Pressure Threshold Value 1|High Pressure Threshold Value 1|High Pressure Threshold Value 1|High Pressure Threshold Value 1|
|…|…|…|…|…|…|…|…|
|High Pressure Threshold Value N|High Pressure Threshold Value N|High Pressure Threshold Value N|High Pressure Threshold Value N|High Pressure Threshold Value N|High Pressure Threshold Value N|High Pressure Threshold Value N|High Pressure Threshold Value N|
|Low Pressure Threshold Preci-<br>sion|Low Pressure Threshold Preci-<br>sion|Low Pressure Threshold Preci-<br>sion|Low Pressure Threshold<br>Scale=kPa|Low Pressure Threshold<br>Scale=kPa|Low Pressure Threshold Size|Low Pressure Threshold Size|Low Pressure Threshold Size|
|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|Low Pressure Threshold Value 1|
|…|…|…|…|…|…|…|…|
|Low Pressure Threshold Value N|Low Pressure Threshold Value N|Low Pressure Threshold Value N|Low Pressure Threshold Value N|Low Pressure Threshold Value N|Low Pressure Threshold Value N|Low Pressure Threshold Value N|Low Pressure Threshold Value N|
|Sensor Polarity|Sensor Polarity|Sensor Polarity|Sensor Polarity|Sensor Polarity|Sensor Polarity|Sensor Polarity|Sensor Polarity|


CC:006B.01.07.11.001 For fields’ description, refer to Section 2.2.51.8 Irrigation System Config Set Command. A sending
node MUST comply with field descriptions in Section 2.2.51.8 Irrigation System Config Set Command.


**2.2.51.11** **Irrigation** **Valve** **Info** **Get** **Command**


This command is used to request general information about the specified valve.


CC:006B.01.08.11.001 The Irrigation Valve Info Report Command MUST be returned in response to this command.


CC:006B.01.08.11.002 This command MUST NOT be issued via multicast addressing.


CC:006B.01.08.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.317: Irrigation Valve Info Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_VALVE_INFO_GET|Command = IRRIGATION_VALVE_INFO_GET|Command = IRRIGATION_VALVE_INFO_GET|Command = IRRIGATION_VALVE_INFO_GET|Command = IRRIGATION_VALVE_INFO_GET|Command = IRRIGATION_VALVE_INFO_GET|Command = IRRIGATION_VALVE_INFO_GET|Command = IRRIGATION_VALVE_INFO_GET|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Main Valve|
|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|



**Reserved**

CC:006B.01.08.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Main** **Valve** **(1** **bit)**

This field is used to indicate whether the sending node requests the information of the main valve or
of a zone valve.


CC:006B.01.08.11.005 The value 1 MUST indicate that the sending node requests the main valve information.


CC:006B.01.08.11.006 The value 0 MUST indicate that the sending node requests information related to the zone valve
corresponding to Valve ID field.


**Valve** **ID** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 267




<!-- PAGE 269 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to indicate the Valve ID if the sending node requests the information about a zone
valve.

CC:006B.01.08.11.007 This field MUST be set to a Valve ID supported by the receiving node.


CC:006B.01.08.12.001 A node receiving this command for an unsupported zone valve ID SHOULD return a report for the
first supported zone valve.

CC:006B.01.08.11.008 If the Main Valve field is set to 1, this field MUST be set to 1. Other values MUST be ignored by a
receiving node.


**2.2.51.12** **Irrigation** **Valve** **Info** **Report** **Command**


This command is used to advertise general information about a given valve.


Table 2.318: Irrigation Valve Info Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_VALVE_INFO_REPORT|Command = IRRIGATION_VALVE_INFO_REPORT|Command = IRRIGATION_VALVE_INFO_REPORT|Command = IRRIGATION_VALVE_INFO_REPORT|Command = IRRIGATION_VALVE_INFO_REPORT|Command = IRRIGATION_VALVE_INFO_REPORT|Command = IRRIGATION_VALVE_INFO_REPORT|Command = IRRIGATION_VALVE_INFO_REPORT|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Conn- ected|Main Valve|
|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|
|Nominal Current|Nominal Current|Nominal Current|Nominal Current|Nominal Current|Nominal Current|Nominal Current|Nominal Current|
|Valve Error Status|Valve Error Status|Valve Error Status|Valve Error Status|Valve Error Status|Valve Error Status|Valve Error Status|Valve Error Status|



**Reserved**

CC:006B.01.09.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Main** **Valve** **(1** **bit)**

This field is used to indicate whether the sending node advertises the information of the main valve
or of a zone valve.


CC:006B.01.09.11.002 The value 1 MUST indicate that the sending node advertises the main valve information.


CC:006B.01.09.11.003 The value 0 MUST indicate that the sending node advertises information related to the zone valve
corresponding to Valve ID field.


**Connected** **(1** **bit)**

This field indicates if the actual valve is currently connected to the node or not.


CC:006B.01.09.11.004 The value 0 MUST indicate that the valve is disconnected from the node.


CC:006B.01.09.11.005 The value 1 MUST indicate that the valve is connected to the node.


**Valve** **ID** **(8** **bits)**

This field is used to indicate the Valve ID if the sending node requests the information about a zone
valve.

CC:006B.01.09.11.006 This field MUST be set to a Valve ID supported by the receiving node.

CC:006B.01.09.11.007 If the Main Valve field is set to 1, this field MUST be set to 1. Other values MUST be ignored by a
receiving node.


**Nominal** **Current** **(8** **bits)**

This field is used to advertise the valve’s nominal electric current when the valve is On / Open.

CC:006B.01.09.11.008 This field MUST be expressed as a multiple of 10mA. E.g. the value 23 represents 230 mA.

CC:006B.01.09.11.009 This field MUST be set to 0 if the Connected field is set to 0.

CC:006B.01.09.11.00A This field MUST advertise the last measured current (measured when the valve was on) when the
valve is Off / Closed.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 268




<!-- PAGE 270 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Valve** **Error** **Status** **(8** **bits)**

CC:006B.01.09.11.00B This bit mask provides valve error status fields. The field MUST be encoded according the following:


      - Bit 0 indicates short circuit has been detected.


      - Bit 1 indicates current high threshold has been detected.


      - Bit 2 indicates current low threshold has been detected.

      - Bit 3 indicates maximum flow has been detected (zone valves only).

      - Bit 4 indicates flow high threshold has been detected (zone valves only).

      - Bit 5 indicates flow low threshold has been detected (zone valves only).


      - Bits 6-7 are reserved.

Any inactive errors can be cleared by sending an Irrigation Valve Config Set Command. Also, if the
valve is turned on again, any inactive errors should be cleared as the valve is turned on.


**2.2.51.13** **Irrigation** **Valve** **Config** **Set** **Command**


This command allows an irrigation valve to be configured accordingly.


Table 2.319: Irrigation Valve Config Set Command



|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_VALVE_CONFIG_SET|Command = IRRIGATION_VALVE_CONFIG_SET|Command = IRRIGATION_VALVE_CONFIG_SET|Command = IRRIGATION_VALVE_CONFIG_SET|Command = IRRIGATION_VALVE_CONFIG_SET|Command = IRRIGATION_VALVE_CONFIG_SET|Command = IRRIGATION_VALVE_CONFIG_SET|Command = IRRIGATION_VALVE_CONFIG_SET|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Main<br>Valve|
|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|
|Nominal Current High Threshold|Nominal Current High Threshold|Nominal Current High Threshold|Nominal Current High Threshold|Nominal Current High Threshold|Nominal Current High Threshold|Nominal Current High Threshold|Nominal Current High Threshold|
|Nominal Current Low Threshold|Nominal Current Low Threshold|Nominal Current Low Threshold|Nominal Current Low Threshold|Nominal Current Low Threshold|Nominal Current Low Threshold|Nominal Current Low Threshold|Nominal Current Low Threshold|
|Maximum Flow Precision|Maximum Flow Precision|Maximum Flow Precision|Maximum Flow Scale=l/h|Maximum Flow Scale=l/h|Maximum Flow Size|Maximum Flow Size|Maximum Flow Size|
|Maximum Flow Value 1|Maximum Flow Value 1|Maximum Flow Value 1|Maximum Flow Value 1|Maximum Flow Value 1|Maximum Flow Value 1|Maximum Flow Value 1|Maximum Flow Value 1|
|…|…|…|…|…|…|…|…|
|Maximum Flow Value N|Maximum Flow Value N|Maximum Flow Value N|Maximum Flow Value N|Maximum Flow Value N|Maximum Flow Value N|Maximum Flow Value N|Maximum Flow Value N|
|Flow High Threshold Precision|Flow High Threshold Precision|Flow High Threshold Precision|Flow High Threshold<br>Scale=l/h|Flow High Threshold<br>Scale=l/h|Flow High Threshold Size|Flow High Threshold Size|Flow High Threshold Size|
|Flow High Threshold Value 1|Flow High Threshold Value 1|Flow High Threshold Value 1|Flow High Threshold Value 1|Flow High Threshold Value 1|Flow High Threshold Value 1|Flow High Threshold Value 1|Flow High Threshold Value 1|
|…|…|…|…|…|…|…|…|
|Flow High Threshold Value N|Flow High Threshold Value N|Flow High Threshold Value N|Flow High Threshold Value N|Flow High Threshold Value N|Flow High Threshold Value N|Flow High Threshold Value N|Flow High Threshold Value N|
|Flow Low Threshold Precision|Flow Low Threshold Precision|Flow Low Threshold Precision|Flow Low Threshold<br>Scale=l/h|Flow Low Threshold<br>Scale=l/h|Flow Low Threshold Size|Flow Low Threshold Size|Flow Low Threshold Size|
|Flow Low Threshold Value 1|Flow Low Threshold Value 1|Flow Low Threshold Value 1|Flow Low Threshold Value 1|Flow Low Threshold Value 1|Flow Low Threshold Value 1|Flow Low Threshold Value 1|Flow Low Threshold Value 1|
|…|…|…|…|…|…|…|…|
|Flow Low Threshold Value N|Flow Low Threshold Value N|Flow Low Threshold Value N|Flow Low Threshold Value N|Flow Low Threshold Value N|Flow Low Threshold Value N|Flow Low Threshold Value N|Flow Low Threshold Value N|
|Sensor Usage|Sensor Usage|Sensor Usage|Sensor Usage|Sensor Usage|Sensor Usage|Sensor Usage|Sensor Usage|


**Reserved**





CC:006B.01.0A.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Main** **Valve** **(1** **bit)**

This field is used to indicate whether the valve to configure is the main valve or a zone valve.

CC:006B.01.0A.11.002 The value 1 MUST indicate that the valve to configure is the main valve.

CC:006B.01.0A.11.003 The value 0 MUST indicate that the valve to configure is the zone valve corresponding to Valve ID
field.


**Valve** **ID** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 269




<!-- PAGE 271 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to indicate the Valve ID to configure.

CC:006B.01.0A.11.004 This field MUST be set to a Valve ID supported by the receiving node.

CC:006B.01.0A.11.005 If the Main Valve field is set to 1, this field MUST be set to 1. Other values MUST be ignored by a
receiving node.


**Nominal** **Current** **High** **Threshold** **(8** **bits)**

This field is used to configure the nominal current high threshold for the actual valve.


CC:006B.01.0A.11.006 The receiving node MUST issue an Irrigation System Status Report Command with the System Error
Status indicating that a valve is reporting errors when the current crosses above this threshold.

CC:006B.01.0A.11.007 This field MUST be expressed as a multiple of 10mA. E.g. the value 23 represents 230 mA.


**Nominal** **Current** **Low** **Threshold** **(8** **bits)**

This field is used to configure the nominal current low threshold for the actual valve at the receiving
node.


CC:006B.01.0A.11.008 The receiving node MUST issue an Irrigation System Status Report Command with the System Error
Status indicating that a valve is reporting errors when the current crosses below this threshold.

CC:006B.01.0A.11.009 This field MUST be expressed as a multiple of 10mA. E.g. the value 23 represents 230 mA.


**Maximum** **Flow**

These fields are used to configure the maximum allowed water flow for the specified valve.

CC:006B.01.0A.11.00A These fields MUST be ignored if the Main Valve field is set to 1.

CC:006B.01.0A.13.001 A receiving node having no support for flow sensor MAY ignore these fields.


CC:006B.01.0A.11.00B
If the receiving node supports a flow sensor, the node MUST issue an Irrigation System Status Report
Command with the System Error Status indicating that a valve is reporting errors when the water
flow crosses above this threshold.

CC:006B.01.0A.11.00C This field MUST be expressed in l/h (liter/hour).


**Flow** **High** **Threshold**

These fields are used to configure the flow high threshold for the specified valve.

CC:006B.01.0A.11.00D These fields MUST be ignored if the Main Valve field is set to 1.

CC:006B.01.0A.13.002 A receiving node having no support for flow sensor MAY ignore these fields.


CC:006B.01.0A.11.00E
If the receiving node supports a flow sensor, the node MUST issue an Irrigation System Status Report
Command with the System Error Status indicating that a valve is reporting errors when the water
flow crosses above this threshold.

CC:006B.01.0A.11.00F The format of the Flow High Threshold fields MUST comply with the format used by the Multilevel
Sensor Command Class and MUST be expressed in l/h (liter/hour).


**Flow** **Low** **Threshold**

These fields are used to configure the flow low threshold for the specified valve.

CC:006B.01.0A.11.010 These fields MUST be ignored if the Main Valve field is set to 1.

CC:006B.01.0A.13.003 A receiving node having no support for flow sensor MAY ignore these fields.


CC:006B.01.0A.11.011
If the receiving node supports a flow sensor, the node MUST issue an Irrigation System Status Report
Command with the System Error Status indicating that a valve is reporting errors when the water
flow crosses below this threshold.

CC:006B.01.0A.11.012 The format of the Flow Low Threshold fields MUST comply with the format used by the Multilevel
Sensor Command Class and MUST be expressed in l/h (liter/hour).


**Sensor** **Usage** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 270




<!-- PAGE 272 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to configure if the actual valve must turn off / close when the specified sensors are
active.

CC:006B.01.0A.11.013 This field MUST be ignored if the Main Valve field is set to 1.

CC:006B.01.0A.11.014 This field MUST be treated as a bit mask and MUST comply with Table 2.320, Irrigation Valve Config
Set::Sensor Usage.


Table 2.320: Irrigation Valve Config Set::Sensor Usage

|Bit|Description|
|---|---|
|0|Use Rain Sensor<br>The valve MUST turn of / close if rain is detected<br>A receiving node having no support for rain sensor MAY ignore this feld.|
|1|Use Moisture Sensor<br>The valve MUST turn of / close if moisture is detected<br>A receiving node having no support for moisture sensor MAY ignore this<br>feld.|
|2..7|_Reserved_|



CC:006B.01.0A.11.015 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**2.2.51.14** **Irrigation** **Valve** **Config** **Get** **Command**


This command is used to request the current configuration of an irrigation valve.

CC:006B.01.0B.11.001 The Irrigation Valve Config Report Command MUST be returned in response to this command.


CC:006B.01.0B.11.002 This command MUST NOT be issued via multicast addressing.


CC:006B.01.0B.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.321: Irrigation Valve Config Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_VALVE_CONFIG_GET|Command = IRRIGATION_VALVE_CONFIG_GET|Command = IRRIGATION_VALVE_CONFIG_GET|Command = IRRIGATION_VALVE_CONFIG_GET|Command = IRRIGATION_VALVE_CONFIG_GET|Command = IRRIGATION_VALVE_CONFIG_GET|Command = IRRIGATION_VALVE_CONFIG_GET|Command = IRRIGATION_VALVE_CONFIG_GET|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Main Valve|
|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|



**Reserved**

CC:006B.01.0B.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Main** **Valve** **(1** **bit)**

This field is used to indicate whether the sending node requests the configuration of the main valve
or of a zone valve.

CC:006B.01.0B.11.005 The value 1 MUST indicate that the sending node requests the main valve configuration.


CC:006B.01.0B.11.006
The value 0 MUST indicate that the sending node requests the configuration related to the zone valve
corresponding to Valve ID field.


**Valve** **ID** **(8** **bits)**

This field is used to indicate the Valve ID if the sending node requests the information about a zone
valve.

CC:006B.01.0B.11.007 This field MUST be set to a Valve ID supported by the receiving node. A node receiving this command

CC:006B.01.0B.12.001 for an unsupported zone valve ID SHOULD return a report for the first supported zone valve.


CC:006B.01.0B.11.008


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 271




<!-- PAGE 273 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If the Main Valve field is set to 1, this field MUST be set to 1. Other values MUST be ignored by a
receiving node.


**2.2.51.15** **Irrigation** **Valve** **Config** **Report** **Command**


This command is used to advertise the configuration of a valve.


Table 2.322: Irrigation Valve Config Report Command






|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_VALVE_CONFIG_REPORT|Command = IRRIGATION_VALVE_CONFIG_REPORT|Command = IRRIGATION_VALVE_CONFIG_REPORT|Command = IRRIGATION_VALVE_CONFIG_REPORT|Command = IRRIGATION_VALVE_CONFIG_REPORT|Command = IRRIGATION_VALVE_CONFIG_REPORT|Command = IRRIGATION_VALVE_CONFIG_REPORT|Command = IRRIGATION_VALVE_CONFIG_REPORT|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Main<br>Valve|
|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|
|Nominal Current High Threshold|Nominal Current High Threshold|Nominal Current High Threshold|Nominal Current High Threshold|Nominal Current High Threshold|Nominal Current High Threshold|Nominal Current High Threshold|Nominal Current High Threshold|
|Nominal Current Low Threshold|Nominal Current Low Threshold|Nominal Current Low Threshold|Nominal Current Low Threshold|Nominal Current Low Threshold|Nominal Current Low Threshold|Nominal Current Low Threshold|Nominal Current Low Threshold|
|Maximum Flow Precision|Maximum Flow Precision|Maximum Flow Precision|Maximum Flow Scale=l/h|Maximum Flow Scale=l/h|Maximum Flow Size|Maximum Flow Size|Maximum Flow Size|
|Maximum Flow Value 1|Maximum Flow Value 1|Maximum Flow Value 1|Maximum Flow Value 1|Maximum Flow Value 1|Maximum Flow Value 1|Maximum Flow Value 1|Maximum Flow Value 1|
|…|…|…|…|…|…|…|…|
|Maximum Flow Value N|Maximum Flow Value N|Maximum Flow Value N|Maximum Flow Value N|Maximum Flow Value N|Maximum Flow Value N|Maximum Flow Value N|Maximum Flow Value N|
|Flow High Threshold Precision|Flow High Threshold Precision|Flow High Threshold Precision|Flow High Threshold<br>Scale=l/h|Flow High Threshold<br>Scale=l/h|Flow High Threshold Size|Flow High Threshold Size|Flow High Threshold Size|
|Flow High Threshold Value 1|Flow High Threshold Value 1|Flow High Threshold Value 1|Flow High Threshold Value 1|Flow High Threshold Value 1|Flow High Threshold Value 1|Flow High Threshold Value 1|Flow High Threshold Value 1|
|…|…|…|…|…|…|…|…|
|Flow High Threshold Value N|Flow High Threshold Value N|Flow High Threshold Value N|Flow High Threshold Value N|Flow High Threshold Value N|Flow High Threshold Value N|Flow High Threshold Value N|Flow High Threshold Value N|
|Flow Low Threshold Precision|Flow Low Threshold Precision|Flow Low Threshold Precision|Flow Low Threshold<br>Scale=l/h|Flow Low Threshold<br>Scale=l/h|Flow Low Threshold Size|Flow Low Threshold Size|Flow Low Threshold Size|
|Flow Low Threshold Value 1|Flow Low Threshold Value 1|Flow Low Threshold Value 1|Flow Low Threshold Value 1|Flow Low Threshold Value 1|Flow Low Threshold Value 1|Flow Low Threshold Value 1|Flow Low Threshold Value 1|
|…|…|…|…|…|…|…|…|
|Flow Low Threshold Value N|Flow Low Threshold Value N|Flow Low Threshold Value N|Flow Low Threshold Value N|Flow Low Threshold Value N|Flow Low Threshold Value N|Flow Low Threshold Value N|Flow Low Threshold Value N|
|Sensor Usage|Sensor Usage|Sensor Usage|Sensor Usage|Sensor Usage|Sensor Usage|Sensor Usage|Sensor Usage|



For fields’ description, refer to Section 2.2.51.13 Irrigation Valve Config Set Command.

CC:006B.01.0C.11.001 A sending node MUST comply with field descriptions in Section 2.2.51.13 Irrigation Valve Config Set
Command.


**2.2.51.16** **Irrigation** **Valve** **Run** **Command**


The Irrigation Valve Run Command will run the specified valve for a specified duration.


Table 2.323: Irrigation Valve Run Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_VALVE_RUN|Command = IRRIGATION_VALVE_RUN|Command = IRRIGATION_VALVE_RUN|Command = IRRIGATION_VALVE_RUN|Command = IRRIGATION_VALVE_RUN|Command = IRRIGATION_VALVE_RUN|Command = IRRIGATION_VALVE_RUN|Command = IRRIGATION_VALVE_RUN|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Main Valve|
|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|Valve ID|
|Duration MSB|Duration MSB|Duration MSB|Duration MSB|Duration MSB|Duration MSB|Duration MSB|Duration MSB|
|Duration LSB|Duration LSB|Duration LSB|Duration LSB|Duration LSB|Duration LSB|Duration LSB|Duration LSB|



**Reserved**

CC:006B.01.0D.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Main** **Valve** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 272




<!-- PAGE 274 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to indicate if the specified valve is the main valve or a zone valve.

CC:006B.01.0D.11.002 The value 1 MUST indicate that the specified valve is the main valve.

CC:006B.01.0D.11.003 The value 0 MUST indicate that the specified valve is the zone valve corresponding to Valve ID field.


**Valve** **ID** **(8** **bits)**

This field is used to specify the actual Valve ID.

CC:006B.01.0D.11.004 This field MUST be set to a Valve ID supported by the receiving node.

CC:006B.01.0D.11.005 If the Main Valve field is set to 1, this field MUST be set to 1. Other values MUST be ignored by a
receiving node.


**Duration** **(16** **bits)**

This field is used to specify the duration of the run in seconds.

CC:006B.01.0D.11.006 The value 0 MUST indicate that the valve MUST be turned off / Closed immediately.


**2.2.51.17** **Irrigation** **Valve** **Table** **Set** **Command**


This command is used to set a valve table with a list of valves and durations.


Table 2.324: Irrigation Valve Table Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_VALVE_TABLE_SET|Command = IRRIGATION_VALVE_TABLE_SET|Command = IRRIGATION_VALVE_TABLE_SET|Command = IRRIGATION_VALVE_TABLE_SET|Command = IRRIGATION_VALVE_TABLE_SET|Command = IRRIGATION_VALVE_TABLE_SET|Command = IRRIGATION_VALVE_TABLE_SET|Command = IRRIGATION_VALVE_TABLE_SET|
|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|
|Valve ID 1|Valve ID 1|Valve ID 1|Valve ID 1|Valve ID 1|Valve ID 1|Valve ID 1|Valve ID 1|
|Duration MSB 1|Duration MSB 1|Duration MSB 1|Duration MSB 1|Duration MSB 1|Duration MSB 1|Duration MSB 1|Duration MSB 1|
|Duration LSB 1|Duration LSB 1|Duration LSB 1|Duration LSB 1|Duration LSB 1|Duration LSB 1|Duration LSB 1|Duration LSB 1|
|…|…|…|…|…|…|…|…|
|Valve ID N|Valve ID N|Valve ID N|Valve ID N|Valve ID N|Valve ID N|Valve ID N|Valve ID N|
|Duration MSB N|Duration MSB N|Duration MSB N|Duration MSB N|Duration MSB N|Duration MSB N|Duration MSB N|Duration MSB N|
|Duration LSB N|Duration LSB N|Duration LSB N|Duration LSB N|Duration LSB N|Duration LSB N|Duration LSB N|Duration LSB N|



**Valve** **Table** **ID** **(8** **bits)**

This field is used to specify the valve table ID.

CC:006B.01.0E.11.001 This field MUST be set to a Valve Table ID supported by the receiving node.


**Valve** **ID** **and** **Duration** **(N** ***** **3** **bytes)**

These fields are used to specify valve IDs and their associated run duration.


CC:006B.01.0E.11.002 A sending node MUST NOT specify more Valve IDs than the “Valve Table Max Size” advertised by
a receiving node in the Irrigation System Info Report Command


CC:006B.01.0E.11.003 The duration MUST be expressed in seconds.

CC:006B.01.0E.13.001 This field MAY be omitted in order to erase/empty the specified valve table.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 273




<!-- PAGE 275 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.51.18** **Irrigation** **Valve** **Table** **Get** **Command**


This command is used to request the contents of the specified Valve Table ID.


CC:006B.01.0F.11.001 The Irrigation Valve Table Report Command MUST be returned in response to this command.


CC:006B.01.0F.11.002 This command MUST NOT be issued via multicast addressing.


CC:006B.01.0F.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.325: Irrigation Valve Table Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_VALVE_TABLE_GET|Command = IRRIGATION_VALVE_TABLE_GET|Command = IRRIGATION_VALVE_TABLE_GET|Command = IRRIGATION_VALVE_TABLE_GET|Command = IRRIGATION_VALVE_TABLE_GET|Command = IRRIGATION_VALVE_TABLE_GET|Command = IRRIGATION_VALVE_TABLE_GET|Command = IRRIGATION_VALVE_TABLE_GET|
|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|



**Valve** **Table** **ID** **(8** **bits)**

This field is used to specify the valve table ID.

CC:006B.01.0F.11.004 Valves tables MUST be identified sequentially from 1 to the total number available on the device.


**2.2.51.19** **Irrigation** **Valve** **Table** **Report** **Command**


This command provides the contents of the specified Valve Table ID.


Table 2.326: Irrigation Valve Table Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_VALVE_TABLE_REPORT|Command = IRRIGATION_VALVE_TABLE_REPORT|Command = IRRIGATION_VALVE_TABLE_REPORT|Command = IRRIGATION_VALVE_TABLE_REPORT|Command = IRRIGATION_VALVE_TABLE_REPORT|Command = IRRIGATION_VALVE_TABLE_REPORT|Command = IRRIGATION_VALVE_TABLE_REPORT|Command = IRRIGATION_VALVE_TABLE_REPORT|
|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|Valve Table ID|
|Valve ID 1|Valve ID 1|Valve ID 1|Valve ID 1|Valve ID 1|Valve ID 1|Valve ID 1|Valve ID 1|
|Duration MSB 1|Duration MSB 1|Duration MSB 1|Duration MSB 1|Duration MSB 1|Duration MSB 1|Duration MSB 1|Duration MSB 1|
|Duration LSB 1|Duration LSB 1|Duration LSB 1|Duration LSB 1|Duration LSB 1|Duration LSB 1|Duration LSB 1|Duration LSB 1|
|…|…|…|…|…|…|…|…|
|Valve ID N|Valve ID N|Valve ID N|Valve ID N|Valve ID N|Valve ID N|Valve ID N|Valve ID N|
|Duration MSB N|Duration MSB N|Duration MSB N|Duration MSB N|Duration MSB N|Duration MSB N|Duration MSB N|Duration MSB N|
|Duration LSB N|Duration LSB N|Duration LSB N|Duration LSB N|Duration LSB N|Duration LSB N|Duration LSB N|Duration LSB N|



For fields’ description, refer to Section 2.2.51.17 Irrigation Valve Table Set Command.

CC:006B.01.10.11.001 A sending node MUST comply with field descriptions in Section 2.2.51.17 Irrigation Valve Table Set
Command.


**2.2.51.20** **Irrigation** **Valve** **Table** **Run** **Command**


This command is used to run the specified valve tables sequentially.


Table 2.327: Irrigation Valve Table Run Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_VALVE_TABLE_RUN|Command = IRRIGATION_VALVE_TABLE_RUN|Command = IRRIGATION_VALVE_TABLE_RUN|Command = IRRIGATION_VALVE_TABLE_RUN|Command = IRRIGATION_VALVE_TABLE_RUN|Command = IRRIGATION_VALVE_TABLE_RUN|Command = IRRIGATION_VALVE_TABLE_RUN|Command = IRRIGATION_VALVE_TABLE_RUN|
|Valve Table ID 1|Valve Table ID 1|Valve Table ID 1|Valve Table ID 1|Valve Table ID 1|Valve Table ID 1|Valve Table ID 1|Valve Table ID 1|
|…|…|…|…|…|…|…|…|
|Valve Table ID N|Valve Table ID N|Valve Table ID N|Valve Table ID N|Valve Table ID N|Valve Table ID N|Valve Table ID N|Valve Table ID N|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 274




<!-- PAGE 276 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Valve** **Table** **ID** **(N** **bytes)**

This field is used to specify the list of Valve Tables to run sequentially.

CC:006B.01.11.11.001 A receiving node MUST run the indicated Valve Table ID starting by the entry 1. These fields contain
a variable list of valve table IDs that will be run sequentially in the order they are listed.


**2.2.51.21** **Irrigation** **System** **Shutoff** **Command**


This command is used to prevent any irrigation activity triggered by the Schedule CC for a specified
duration.


Table 2.328: Irrigation System Shutoff Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|Command Class = COMMAND_CLASS_IRRIGATION|
|Command = IRRIGATION_SYSTEM_SHUTOFF|Command = IRRIGATION_SYSTEM_SHUTOFF|Command = IRRIGATION_SYSTEM_SHUTOFF|Command = IRRIGATION_SYSTEM_SHUTOFF|Command = IRRIGATION_SYSTEM_SHUTOFF|Command = IRRIGATION_SYSTEM_SHUTOFF|Command = IRRIGATION_SYSTEM_SHUTOFF|Command = IRRIGATION_SYSTEM_SHUTOFF|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|



**Duration** **(8** **bits)**

This field is used to indicate the duration of the system shutoff.



CC:006B.01.12.11.001


CC:006B.01.12.11.002


CC:006B.01.12.11.003



Values in the range 1..254 MUST indicate how many hours the irrigation system MUST stay shut
off after reception of this command. While active, the shutoff duration MUST prevent all enabled
schedules (including the back-up schedule) from running. After the shutoff duration is over, any
enabled schedule MUST run as configured.



CC:006B.01.12.11.004 The value 0 MUST indicate to turn off any running valve (including the main valve) as well as cancel

CC:006B.01.12.11.005 any active Irrigation Valve Table Run or Schedule. Any subsequent schedule MUST run as configured.

CC:006B.01.12.11.006 The value 255 MUST indicate that the irrigation system MUST stay permanently shut off until the
node receives one of the following commands:

      - Irrigation System Shutoff Command with a Duration different than 255.


      - Irrigation Valve Run Command


      - Irrigation Valve Table Run Command

CC:006B.01.12.11.007 When permanently shut off, the node MUST NOT run any schedule


CC:006B.01.12.11.008
A receiving node MUST cancel the current shutoff and advertise a shutoff duration of 0 in the Irrigation
System Status Report Command after receiving one of the following commands:


      - Irrigation Valve Run Command


      - Irrigation Valve Table Run Command


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 275