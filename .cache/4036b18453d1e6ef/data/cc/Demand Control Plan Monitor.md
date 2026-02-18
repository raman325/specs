<!-- PAGE 181 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.36** **Demand** **Control** **Plan** **Monitor** **Command** **Class,** **version** **1**


The Demand Control Plan Monitor Command Class allows devices to monitor the list of Demand
Control Plan (DCP). A DCP event contains information regarding criticality, products involved,
requested reduction, time duration and if a certain rate (identified by a Demand Control Plan Rate
ID, refer to the Rate Table Configuration Command Class) is associated with the event. When a DCP
event is outdated, it is removed from the list. Each DCP event is uniquely identified by a timestamp
issued the Utility Supplier.


**2.2.36.1** **DCP** **list** **get** **command**


This command is used to request the pending DCP event in a device.


The DCP List Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.178: DCP List Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|
|Command = DCP_LIST_GET|Command = DCP_LIST_GET|Command = DCP_LIST_GET|Command = DCP_LIST_GET|Command = DCP_LIST_GET|Command = DCP_LIST_GET|Command = DCP_LIST_GET|Command = DCP_LIST_GET|



**2.2.36.2** **DCP** **list** **report** **command**


This command reports the pending DCP event in a device. If more than one DCP event is pending the reports will be submitted in chronically order as to when the events was placed on the list. Newest
entry will be reported first.


Table 2.179: DCP List Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|
|Command = DCP_LIST_REPORT|Command = DCP_LIST_REPORT|Command = DCP_LIST_REPORT|Command = DCP_LIST_REPORT|Command = DCP_LIST_REPORT|Command = DCP_LIST_REPORT|Command = DCP_LIST_REPORT|Command = DCP_LIST_REPORT|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|
|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|
|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|
|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|
|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|
|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|
|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|
|DCP ID|DCP ID|DCP ID|DCP ID|DCP ID|DCP ID|DCP ID|DCP ID|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Number of DC|Number of DC|
|Generic Device Class 1<br>|Generic Device Class 1<br>|Generic Device Class 1<br>|Generic Device Class 1<br>|Generic Device Class 1<br>|Generic Device Class 1<br>|Generic Device Class 1<br>|Generic Device Class 1<br>|
|Specifc Device Class 1|Specifc Device Class 1|Specifc Device Class 1|Specifc Device Class 1|Specifc Device Class 1|Specifc Device Class 1|Specifc Device Class 1|Specifc Device Class 1|
|…|…|…|…|…|…|…|…|
|Generic Device Class N<br>|Generic Device Class N<br>|Generic Device Class N<br>|Generic Device Class N<br>|Generic Device Class N<br>|Generic Device Class N<br>|Generic Device Class N<br>|Generic Device Class N<br>|
|Specifc Device Class N|Specifc Device Class N|Specifc Device Class N|Specifc Device Class N|Specifc Device Class N|Specifc Device Class N|Specifc Device Class N|Specifc Device Class N|
|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|
|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|
|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|
|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|
|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|



continues on next page


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 180




<!-- PAGE 182 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.179 – continued from previous page

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|
|Start Second Local Time|Start Second Local Time|Start Second Local Time|Start Second Local Time|Start Second Local Time|Start Second Local Time|Start Second Local Time|Start Second Local Time|
|Duration Hour Time|Duration Hour Time|Duration Hour Time|Duration Hour Time|Duration Hour Time|Duration Hour Time|Duration Hour Time|Duration Hour Time|
|Duration Minute Time|Duration Minute Time|Duration Minute Time|Duration Minute Time|Duration Minute Time|Duration Minute Time|Duration Minute Time|Duration Minute Time|
|Duration Second Time|Duration Second Time|Duration Second Time|Duration Second Time|Duration Second Time|Duration Second Time|Duration Second Time|Duration Second Time|
|Event Priority|Event Priority|Event Priority|Event Priority|Event Priority|Event Priority|Event Priority|Event Priority|
|Load shedding|Load shedding|Load shedding|Load shedding|Load shedding|Load shedding|Load shedding|Load shedding|
|Start Association Group|Start Association Group|Start Association Group|Start Association Group|Start Association Group|Start Association Group|Start Association Group|Start Association Group|
|Stop Association Group|Stop Association Group|Stop Association Group|Stop Association Group|Stop Association Group|Stop Association Group|Stop Association Group|Stop Association Group|
|Randomization interval|Randomization interval|Randomization interval|Randomization interval|Randomization interval|Randomization interval|Randomization interval|Randomization interval|



**Reports** **to** **Follow** **(8** **bits)**


This value indicates how many report frames there are left, the value 0xFF means that the number
of reports have not been calculated yet or that there is more than 255 reports to follow.

Refer to DCP List Set command class ( _DCP_ _list_ _set_ _command_ ) for detailed description of the fields.


**2.2.36.3** **DCP** **event** **status** **get**


This command is used to query the status of a specific DCP event in the DCP list.


The DCP Event Status Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.180: DCP Event Status Get

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|
|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|
|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|
|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|
|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|
|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|
|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|
|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|
|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|



Refer to DCP List Set command class ( _DCP_ _list_ _set_ _command_ ) for detailed description of the fields.


**2.2.36.4** **DCP** **event** **status** **report**


This command is used to provide the status of a specific DCP event in the DCP list.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 181




<!-- PAGE 183 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.181: DCP Event Status Report

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|Command Class = COMMAND_CLASS_DCP_MONITOR|
|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|Command = DCP_EVENT_STATUS_GET|
|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|Timestamp -Year 1|
|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|Timestamp -Year 2|
|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|Timestamp -Month|
|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|Timestamp -Day|
|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|Timestamp -Hour Local Time|
|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|Timestamp -Minute Local Time|
|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|Timestamp -Second Local Time|
|Event status|Event status|Event status|Event status|Event status|Event status|Event status|Event status|



Refer to DCP List report command class ( _DCP_ _list_ _report_ _command_ ) for description of fields


**Event** **Status** **(8** **bits)**

The field contains the status of the event.

|182: DCP Event Event status|Status Report::Event Status e Description|
|---|---|
|**Event status**|**Description**|
|0x01|Event Started|
|0x02|Event Completed|
|0x03|Event Rejected by the user|
|0x04|Event not Applicable|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 182




<!-- PAGE 184 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.37** **Door** **Lock** **Command** **Class,** **version** **1-2**


The Door Lock Command Class is used to operate and configure a door lock device.


The Door Lock Command Class is an actuator control command class. Refer to Section 2.1.6.


**2.2.37.1** **Compatibility** **considerations**


A device supporting Door Lock CC, Version 2 MUST support Door Lock CC, version 1.


CC:0062.02.00.21.001 The Door Lock Command Class, version 2 adds the “unknown” state to the Door Lock Operation
Report Command.


CC:0062.01.00.21.001 A supporting node MAY implement a subset of the features represented by the Door Lock Mode, Door
Handles Mode and Door Condition fields which are provided by the commands of this Command Class.


**2.2.37.2** **Door** **Lock** **Operation** **Set** **Command**


This command is used to set the operation mode of a supporting door lock device.


Table 2.183: Door Lock Operation Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_OPERATION_SET|Command = DOOR_LOCK_OPERATION_SET|Command = DOOR_LOCK_OPERATION_SET|Command = DOOR_LOCK_OPERATION_SET|Command = DOOR_LOCK_OPERATION_SET|Command = DOOR_LOCK_OPERATION_SET|Command = DOOR_LOCK_OPERATION_SET|Command = DOOR_LOCK_OPERATION_SET|
|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|



**Door** **Lock** **Mode** **(8** **bits)**

The Door Lock Mode field is used to specify the operation mode of the door lock device.

CC:0062.01.01.11.001 The encoding of this field MUST be according to Table 2.184.

|Mode|Table 2.184: Door Lock Operation Set::Mode Description|Version|
|---|---|---|
|Mode|Description|Version|
|0x00|Door Unsecured 1)|1|
|0x01|Door Unsecured with timeout 2)|1|
|0x10|Door Unsecured for inside Door Handles 1)|1|
|0x11|Door Unsecured for inside Door Handles with timeout 2)|1|
|0x20|Door Unsecured for outside Door Handles 1)|1|
|0x21|Door Unsecured for outside Door Handles with timeout 2)|1|
|0xFF|Door Secured|1|



1) Constant mode. Door will be unsecured until set to secured mode by another command.


2) Timeout mode. Fallback to secured mode after timeout has expired.


CC:0062.01.01.11.002 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0062.01.01.11.003 A controlling node MUST NOT specify modes using timeout-based fall back if the Operation Type
of the supporting device is set to Constant operation (set by Door Lock Configuration Set).


CC:0062.01.01.11.004 A supporting node MUST ignore modes using timeout-based fall back if Operation Type is set to
Constant operation.


CC:0062.01.01.11.006 A supporting node MUST apply the constant modes without any timeout even if it is set to Timed
Operation Type.

CC:0062.01.01.13.001 A supporting node MAY implement a subset of the Door Lock Modes defined by Table 36.


CC:0062.01.01.11.005 A supporting node MUST accept the Door Lock Mode values 0x00 and 0xFF.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 183




<!-- PAGE 185 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.37.3** **Door** **Lock** **Operation** **Get** **Command**


This command is used to request the status of a door lock device.


CC:0062.01.02.11.001 The Door Lock Operation Report command MUST be returned in response to this command.


CC:0062.01.02.11.002 This command MUST NOT be issued via multicast addressing.


CC:0062.01.02.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.185: Door Lock Operation Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_OPERATION_GET|Command = DOOR_LOCK_OPERATION_GET|Command = DOOR_LOCK_OPERATION_GET|Command = DOOR_LOCK_OPERATION_GET|Command = DOOR_LOCK_OPERATION_GET|Command = DOOR_LOCK_OPERATION_GET|Command = DOOR_LOCK_OPERATION_GET|Command = DOOR_LOCK_OPERATION_GET|



**2.2.37.4** **Door** **Lock** **Operation** **Report** **Command**


This command is used to advertise the status of a door lock device.


Table 2.186: Door Lock Operation Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|
|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|
|Outside Door Handles Mode|Outside Door Handles Mode|Outside Door Handles Mode|Outside Door Handles Mode|Inside Door Handles Mode|Inside Door Handles Mode|Inside Door Handles Mode|Inside Door Handles Mode|
|Door Condition|Door Condition|Door Condition|Door Condition|Door Condition|Door Condition|Door Condition|Door Condition|
|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|
|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|



**Door** **Lock** **Mode** **(8** **bits)**

CC:0062.01.03.11.001 The Door Lock Mode field MUST advertise the mode of the door lock device.

CC:0062.01.03.11.002 The encoding of this field MUST be according to Table 2.187.


Table 2.187: Door Lock Operation Report::Door Lock Mode

|Mode|Description|Version|
|---|---|---|
|0x00|Door Unsecured 1)|1|
|0x01|Door Unsecured with timeout 2)|1|
|0x10|Door Unsecured for inside Door Handles 1)|1|
|0x11|Door Unsecured for inside Door Handles with timeout 2)|1|
|0x20|Door Unsecured for outside Door Handles 1)|1|
|0x21|Door Unsecured for outside Door Handles with timeout 2)|1|
|0xFE|Door/Lock State Unknown 3)|2|
|0xFF|Door Secured|1|



1) Constant mode. Door will be unsecured until set back to secured mode by command


2) Timeout mode. Fallback to secured mode after timeout has expired


3) Bolt is not fully retracted/engaged


CC:0062.01.03.11.003 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0062.01.03.13.001 A supporing node MAY advertise a subset of the available Door Lock Mode values.


CC:0062.01.03.11.004


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 184




<!-- PAGE 186 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A controlling node MUST accept all Door Lock Mode values.

CC:0062.01.03.12.001 The Door Lock Mode field SHOULD advertise the current value of the device hardware; also while in
transition to a new target value.


**Outside** **Door** **Handles** **Mode** **(4** **bits)**

CC:0062.01.03.11.005 This field MUST advertise the status of each individual outside door handle.

CC:0062.01.03.11.006 The encoding of the Outside Door Handles Mode bitmask field MUST be according to Table 2.188
and Table 2.189.


Table 2.188: Door Handles Mode bitmask

|Bit 3|Bit 2|Bit 1|Bit 0|
|---|---|---|---|
|Handle 4|Handle 3|Handle 2|Handle 1|



Table 2.189: Door Handles Mode bit encoding

|Bit value|Description|
|---|---|
|‘0’|Disabled|
|‘1’|Enabled|



CC:0062.01.03.11.007 The value ‘0’ MUST signify that the actual handle cannot open the door locally.


CC:0062.01.03.11.008 The value ‘1’ MUST signify that the actual handle can open the door locally.


CC:0062.01.03.13.002 A supporting node MAY advertise just a subset of the available Door Handles Mode values.


CC:0062.01.03.11.009 A controlling node MUST accept all Door Handles Mode values.


**Inside** **Door** **Handles** **Mode** **(4** **bits)**

CC:0062.01.03.11.00A This field MUST advertise the status of each individual inside door handle.

CC:0062.01.03.11.00B The encoding of the Inside Door Handles Mode bitmask field MUST be according to Table 2.188 and
Table 2.189.


CC:0062.01.03.13.003 A supporting node MAY advertise just a subset of the available Door Handles Mode values.


CC:0062.01.03.11.00C A controlling node MUST accept all Door Handles Mode values.


**Door** **Condition** **(8** **bits)**

CC:0062.01.03.11.00D The Door Condition field MUST advertise the status of the door lock components.

CC:0062.01.03.11.00E The encoding of the Door Condition bitmask field MUST be according to Table 2.203.


CC:0062.03.13.004 A supporting node MAY advertise just a subset of the available Door Condition values.


CC:0062.03.11.0010 A controlling node MUST accept all Door Condition values.


**Remaining** **Lock** **Time** **Minutes** **(8** **bits)**


CC:0062.01.03.11.011
This field MUST advertise the remaining time before the door lock will automatically be locked again.

CC:0062.01.03.11.012 The encoding of the _Remaining_ _Lock_ _Time_ _Minutes_ field MUST be according to Table 2.190. The
time the supporting node stays unlocked MUST be determined by combining the _Remaining_ _Lock_
_Time_ _Minutes_ and _Remaining_ _Lock_ _Time_ _Seconds_ fields.


Table 2.190: Door Lock Operation Report::Remaining Lock Time
Minutes


CC:0062.01.03.11.013

|Value|Operation|
|---|---|
|0x00..0xFD|Unlocked 0 .. 253 minutes (Operation Type = Timed Operation)|
|0xFE|No unlocked period (Operation Type = Constant Operation)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 185




<!-- PAGE 187 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0062.01.03.13.005 A supporting node MAY advertise just a subset of the available Remaining Lock Time values.


CC:0062.01.03.11.014 A controlling node MUST accept all Remaining Lock Time values.


**Remaining** **Lock** **Time** **Seconds** **(8** **bits)**


CC:0062.01.03.11.015
This field MUST advertise the remaining time before the door lock will automatically be locked again.

CC:0062.01.03.11.016 The encoding of the Remaining Lock Time Seconds field MUST be according to Table 2.191. The
time to stay unlocked MUST be determined by combining the _Remaining_ _Lock_ _Time_ _Minutes_ and
_Remaining_ _Lock_ _Time_ _Seconds_ fields.


Table 2.191: Door Lock Operation Report::Remaining Lock Time
Seconds

|Value|Operation|
|---|---|
|0..59 (0x00..0x3B)|Unlocked 0 .. 59 seconds (Operation Type = Timed Operation)|
|254 (0xFE)|No unlocked period (Operation Type = Constant Operation)|



CC:0062.01.03.11.017 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0062.01.03.13.006 A supporting node MAY advertise just a subset of the available Lock Timeout values.


CC:0062.01.03.11.018 A controlling de MUST accept all Lock Timeout values.


**2.2.37.5** **Door** **Lock** **Configuration** **Set** **Command**


This command is used to set the configuration of a supporting door lock device.


CC:0062.01.04.11.001 A door lock device MUST be able to operate with the factory default settings.


Table 2.192: Door Lock Configuration Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_CONFIGURATION_SET|Command = DOOR_LOCK_CONFIGURATION_SET|Command = DOOR_LOCK_CONFIGURATION_SET|Command = DOOR_LOCK_CONFIGURATION_SET|Command = DOOR_LOCK_CONFIGURATION_SET|Command = DOOR_LOCK_CONFIGURATION_SET|Command = DOOR_LOCK_CONFIGURATION_SET|Command = DOOR_LOCK_CONFIGURATION_SET|
|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|
|Outside Door Handles Enabled|Outside Door Handles Enabled|Outside Door Handles Enabled|Outside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|
|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|
|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|



**Operation** **Type** **(1** **byte)**

CC:0062.01.04.11.002 The Operation Type field MUST be set according to Table 2.193. When timed operation is specified,
the Lock Timeout Minutes and Lock Timeout Seconds fields MUST be set to valid values.


Table 2.193: Door Lock Operation Type

|Operation Type|Description|Valid Lock Timeout values|
|---|---|---|
|0x01|Constant operation|Minutes<br>=<br>0xFE<br>Sec-<br>onds= 0xFE|
|0x02|Timed operation|Minutes<br>=<br>0x00..0xFD<br>Seconds= 0x00..0x3B|



CC:0062.01.04.11.003 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0062.01.04.13.001 A supporting node MAY accept just a subset of the available Operation Type values.


CC:0062.01.04.11.004


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 186




<!-- PAGE 188 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A supporting node MUST accept the Operation Type value 0x01.


**Outside** **Door** **Handles** **Enabled** **(4** **bits)**

This field is used to advertise the status of each individual outside door handle.

CC:0062.01.04.11.005 The encoding of the Outside Door Handles Mode bitmask field MUST be according to Table 2.188
and Table 2.189.


CC:0062.01.04.13.002 A supporting node MAY ignore the Door Handles Mode value.


**Inside** **Door** **Handles** **Enabled** **(4** **bits)**

CC:0062.01.04.11.006 This field MUST advertise the status of each individual inside door handle.

CC:0062.01.04.11.007 The encoding of the Inside Door Handles Mode bitmask field MUST be according to Table 2.188 and
Table 2.189.


CC:0062.01.04.13.003 A supporting node MAY ignore the Door Handles Mode value.


**Lock** **Timeout** **Minutes** **(1** **byte)**


CC:0062.01.04.11.008
This field MUST specify the time that a door lock must wait before automatically being locked again.

CC:0062.01.04.11.009 The encoding of the Lock Timeout Minutes field MUST be according to Table 2.190. The time to stay
unlocked MUST be determined by combining the _Lock_ _Timeout_ _Minutes_ and _Lock_ _Timeout_ _Seconds_
fields.


CC:0062.01.04.13.004 A supporting node MAY ignore the Lock Timeout values if it implements only the Operation Type
= 0x01 (Constant operation).


**Lock** **Timeout** **Seconds** **(1** **byte)**


CC:0062.01.04.11.00A
This field MUST specify the time that a door lock must wait before automatically being locked again.

CC:0062.01.04.11.00B The encoding of the Lock Timeout Seconds field MUST be according to Table 2.191. The time to stay
unlocked MUST be determined by combining the _Lock_ _Timeout_ _Minutes_ and _Lock_ _Timeout_ _Seconds_
fields.


CC:0062.01.04.13.005 A supporting node MAY ignore the Lock Timeout values if it implements only the Operation Type
= 0x01 (Constant operation).


**2.2.37.6** **Door** **Lock** **Configuration** **Get** **Command**


This command is used to request the configuration parameters of a door lock device.

CC:0062.01.05.11.001 The Door Lock Configuration Report command MUST be returned in response to this command.


CC:0062.01.05.11.002 This command MUST NOT be issued via multicast addressing.


CC:0062.01.05.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.194: Door Lock Configuration Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_CONFIGURATION_GET|Command = DOOR_LOCK_CONFIGURATION_GET|Command = DOOR_LOCK_CONFIGURATION_GET|Command = DOOR_LOCK_CONFIGURATION_GET|Command = DOOR_LOCK_CONFIGURATION_GET|Command = DOOR_LOCK_CONFIGURATION_GET|Command = DOOR_LOCK_CONFIGURATION_GET|Command = DOOR_LOCK_CONFIGURATION_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 187




<!-- PAGE 189 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.37.7** **Door** **Lock** **Configuration** **Report** **Command**


This command is used to advertise the configuration parameters of a door lock device.


Table 2.195: Door Lock Configuration Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_CONFIGURATION_REPORT|Command = DOOR_LOCK_CONFIGURATION_REPORT|Command = DOOR_LOCK_CONFIGURATION_REPORT|Command = DOOR_LOCK_CONFIGURATION_REPORT|Command = DOOR_LOCK_CONFIGURATION_REPORT|Command = DOOR_LOCK_CONFIGURATION_REPORT|Command = DOOR_LOCK_CONFIGURATION_REPORT|Command = DOOR_LOCK_CONFIGURATION_REPORT|
|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|
|Outside Door Handles Enabled|Outside Door Handles Enabled|Outside Door Handles Enabled|Outside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|
|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|
|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|



For fields’ description, refer to Section 2.2.37.5 _Door_ _Lock_ _Configuration_ _Set_ _Command_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 188