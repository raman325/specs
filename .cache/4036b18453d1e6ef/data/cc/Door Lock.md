<!-- PAGE 190 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.38** **Door** **Lock** **Command** **Class,** **version** **3**


The Door Lock Command Class is used to operate and configure a door lock device.


The Door Lock Command Class is an actuator control command class. Refer to Section 2.1.6.

Commands and fields not described in version 3 remain unchanged from version 2.


**2.2.38.1** **Compatibility** **considerations**


CC:0062.03.00.21.001 A node supporting the Door Lock Command Class, version 3 MUST support the Door Lock Command
Class, version 2.


Version 3 adds duration and target value reporting to the Door Lock Operation Report Command.


**2.2.38.2** **Door** **Lock** **Operation** **Report** **Command**


This command is used to advertise the status of a door lock device.


Table 2.196: Door Lock Operation Report Command, version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|Command = DOOR_LOCK_OPERATION_REPORT|
|Current Door Lock Mode|Current Door Lock Mode|Current Door Lock Mode|Current Door Lock Mode|Current Door Lock Mode|Current Door Lock Mode|Current Door Lock Mode|Current Door Lock Mode|
|Outside Door Handles Enabled|Outside Door Handles Enabled|Outside Door Handles Enabled|Outside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|
|Door Condition|Door Condition|Door Condition|Door Condition|Door Condition|Door Condition|Door Condition|Door Condition|
|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|
|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|
|Target Door Lock Mode|Target Door Lock Mode|Target Door Lock Mode|Target Door Lock Mode|Target Door Lock Mode|Target Door Lock Mode|Target Door Lock Mode|Target Door Lock Mode|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|



Fields not described below remain unchanged from previous versions.


**Current** **Door** **Lock** **Mode** **(8** **bits)**

CC:0062.03.03.11.001 The Current Door Lock Mode field MUST advertise the current mode of the door lock device.

CC:0062.03.03.11.002 The encoding of this field MUST be according to Table 2.187.



CC:0062.03.03.12.001



An Operation Set Command may be used to initiate a transition to a new target mode. The device
may be queried for its current mode while in transition to a new mode. The response to an Operation
Get SHOULD be the current mode of the device hardware, e.g. Door/Lock State Unknown. (applies
to Version 2 and newer).


**Target** **Door** **Lock** **Mode** **(8** **bits)**



CC:0062.03.03.11.003 The Target Door Lock Mode field MUST advertise the target mode of an ongoing transition or the
most recent transition.

CC:0062.03.03.11.004 The encoding of this field MUST be according to Table 2.187.


**Duration** **(8** **bits)**

CC:0062.03.03.12.002 The Duration field SHOULD advertise the remaining time before the target mode is reached.

CC:0062.03.03.11.005 The encoding of this field MUST be according to Table 2.8.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 189

---

<!-- PAGE 191 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.39** **Door** **Lock** **Command** **Class,** **version** **4**


**2.2.39.1** **Terminology**


A door lock supports at least 2 **modes** : secured (it cannot be opened with handles) and unsecured
(it can be opened with handles). It may support more modes where the node is for example secured
only for the inside handles.


A door lock may have several components such as a **latch**, a **bolt** and **handles** .


A latch, which can also be called a latch bolt or spring bolt, usually locks the door automatically when
closing it. The latch bolt is disengaged (retracted) typically when the user turns the door handle,
which via the lockset’s mechanism, manually retracts the latch bolt, allowing the door to open.


Handles allow to retract the door’s latch.


A bolt, also named dead bolt and hook bolt, allows to secure the door. When the bolt is out or
extended, the door lock is usually secured (locked) but there are locks that are unlocked even then
the bolt is out which will withdraw the bolt when user turns the door handle (which also retract the
latch). The position of the bolt is not directly related to the Door Lock Mode.


A supporting door lock runs in **constant** **operation** by default. In constant operation, the door lock
stays in the same mode until receiving a new command or being locally actuated. A door lock may
support **timed** **operation** . Timed operation has its own subset of modes, which after being activated
will automatically return to the secured mode after the configured Lock Timeout.


An **auto-relock** functionality can be supported for returning automatically to secured mode some
given time after any operation mode change, including constant operation or changes initiated physically by a user (unlocking with key, thumb turn, etc). Auto-relock should not have any effect when
the lock runs in Timed Operation


A door lock node may have a **twist** **assist** mechanism. When a user starts rotating a key or the
thumb turn to unlock the door, a motor starts rotating to help the user completing the movement. It
can be helpful for disabled users.


A node may support a **hold** **and** **release** functionality for spring latches. This is useful for locks
having a handle that cannot retract the door spring latch on one side. This functionality defines how
long the spring latch must be retracted after the door mode has been changed to unsecured.


A **block-to-block** functionality can be activated for locks having separate lock block on each side of
the door and cannot sense local changes on one side. Enabling the block-to-block feature will make
the door lock try to execute a lock or unlock command on both sides regardless of the last known lock
mode (representing the side that can be sensed). When this feature is disabled, the lock will ignore a
command indicating a mode if it is identical to the last known lock mode.


**2.2.39.2** **Compatibility** **considerations**


The Door Lock Command Class, version 4 is backwards compatible with the Door Lock Command
CC:0062.04.00.21.001 Class, version 3. Fields and commands not mentioned in this version MUST remain unchanged from
the Door Lock Command Class, version 3.


Commands for advertising node capabilities are introduced in this version:


      - Door Lock Capabilities Get Command


      - Door Lock Capabilities Report Command


These commands are extended in order to provide the auto-relock, twist assist and block-to-block
functionalities.

      - Door Lock Configuration Set Command

      - Door Lock Configuration Report Command


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 190




<!-- PAGE 192 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.39.3** **Door** **Lock** **Operation** **Set** **Command**


This command is used to set the mode of a supporting door lock node.


Table 2.197: Door Lock Operation Set Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_OPERATION_SET (0x01)|Command = DOOR_LOCK_OPERATION_SET (0x01)|Command = DOOR_LOCK_OPERATION_SET (0x01)|Command = DOOR_LOCK_OPERATION_SET (0x01)|Command = DOOR_LOCK_OPERATION_SET (0x01)|Command = DOOR_LOCK_OPERATION_SET (0x01)|Command = DOOR_LOCK_OPERATION_SET (0x01)|Command = DOOR_LOCK_OPERATION_SET (0x01)|
|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|Door Lock Mode|



**Door** **Lock** **Mode** **(8** **bits)**

CC:0062.04.01.11.001 This field is used to specify the operation mode that the supporting node MUST assume. This field
MUST be encoded according to Table 2.198.


Table 2.198: Door Lock Operation Set::Mode encoding

|Value|Mode Description|Operation Type|Version|
|---|---|---|---|
|0x00|Door Unsecured|Constant|1|
|0x01|Door Unsecured with timeout|Timed|1|
|0x10|Door Unsecured for inside Door Handles|Constant|1|
|0x11|Door Unsecured for inside Door Handles with<br>timeout|Timed|1|
|0x20|Door Unsecured for outside Door Handles|Constant|1|
|0x21|Door Unsecured for outside Door Handles with<br>timeout|Timed|1|
|0xFF|Door Secured|Constant|1|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0062.04.01.51.001 A controlling node MUST NOT specify modes using timeout-based fall back if the Operation Type
of the supporting device is set to Constant operation (set by Door Lock Configuration Set).


CC:0062.04.01.11.002 A supporting node MUST ignore modes using timeout-based fall back if Operation Type is set to
Constant operation.

CC:0062.04.01.11.003 A supporting node MUST apply the constant modes without any timeout even if it is configured to
run in Timed Operation.

CC:0062.04.01.11.004 A supporting node MUST ignore the command if the value specified in this field is not advertised as
supported in the Door Lock Capabilities Report Command.


CC:0062.04.01.11.005 A supporting node MUST support the door lock mode values 0x00 and 0xFF.


**2.2.39.4** **Door** **Lock** **Operation** **Get** **Command**


This command is used to request the mode of a supporting door lock node.


CC:0062.04.02.11.001 The Door Lock Operation Report Command MUST be returned in response to this command.


CC:0062.04.02.51.001 This command MUST NOT be issued via multicast addressing.


CC:0062.04.02.11.002 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.199: Door Lock Operation Get Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_OPERATION_GET (0x02)|Command = DOOR_LOCK_OPERATION_GET (0x02)|Command = DOOR_LOCK_OPERATION_GET (0x02)|Command = DOOR_LOCK_OPERATION_GET (0x02)|Command = DOOR_LOCK_OPERATION_GET (0x02)|Command = DOOR_LOCK_OPERATION_GET (0x02)|Command = DOOR_LOCK_OPERATION_GET (0x02)|Command = DOOR_LOCK_OPERATION_GET (0x02)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 191




<!-- PAGE 193 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.39.5** **Door** **Lock** **Operation** **Report** **Command**


This command is used to advertise the mode of a supporting door lock node.


Table 2.200: Door Lock Operation Report Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_OPERATION_REPORT (0x03)|Command = DOOR_LOCK_OPERATION_REPORT (0x03)|Command = DOOR_LOCK_OPERATION_REPORT (0x03)|Command = DOOR_LOCK_OPERATION_REPORT (0x03)|Command = DOOR_LOCK_OPERATION_REPORT (0x03)|Command = DOOR_LOCK_OPERATION_REPORT (0x03)|Command = DOOR_LOCK_OPERATION_REPORT (0x03)|Command = DOOR_LOCK_OPERATION_REPORT (0x03)|
|Current Door Lock Mode|Current Door Lock Mode|Current Door Lock Mode|Current Door Lock Mode|Current Door Lock Mode|Current Door Lock Mode|Current Door Lock Mode|Current Door Lock Mode|
|Outside Door Handles Mode|Outside Door Handles Mode|Outside Door Handles Mode|Outside Door Handles Mode|Inside Door Handles Mode|Inside Door Handles Mode|Inside Door Handles Mode|Inside Door Handles Mode|
|Door Condition|Door Condition|Door Condition|Door Condition|Door Condition|Door Condition|Door Condition|Door Condition|
|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|Remaining Lock Time Minutes|
|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|Remaining Lock Time Seconds|
|Target Door Lock Mode|Target Door Lock Mode|Target Door Lock Mode|Target Door Lock Mode|Target Door Lock Mode|Target Door Lock Mode|Target Door Lock Mode|Target Door Lock Mode|
|Duration|Duration|Duration|Duration|Duration|Duration|Duration|Duration|



**Current** **Door** **Lock** **Mode** **(8** **bits)**

CC:0062.04.03.11.001 This field MUST advertise the current door lock mode of the sending node. This field MUST be
encoded according to Table 2.201.


Table 2.201: Door Lock Operation Report::Mode encoding







|Value|Mode Description|Operation Type|Version|
|---|---|---|---|
|0x00|Door Unsecured|Constant (or timed)|1|
|0x01|Door Unsecured with timeout|Timed|1|
|0x10|Door Unsecured for inside Door Handles|Constant (or timed)|1|
|0x11|Door Unsecured for inside Door Handles with<br>timeout|Timed|1|
|0x20|Door Unsecured for outside Door Handles|Constant (or timed)|1|
|0x21|Door Unsecured for outside Door Handles with<br>timeout|Timed|1|
|0xFE|Door mode unknown (e.g.<br>bolt not fully re-<br>tracted)|N/A|2|
|0xFF|Door Secured|Constant (or timed)|1|


All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0062.04.03.12.001
A sending node SHOULD set this field to 0xFE if sending this command while performing a transition
between 2 modes.


**Outside** **Door** **Handles** **Mode** **(4** **bits)**

This field is used to advertise the status of each individual outside door handle.

CC:0062.0403.11.002 This field MUST be treated as a bitmask field and MUST be encoded according to Table 2.202.


Table 2.202: Door Lock Operation Report::Door Handles Mode
bitmask encoding

|Bit 3|Bit 2|Bit 1|Bit 0|
|---|---|---|---|
|Handle 4|Handle 3|Handle 2|Handle 1|



CC:0062.04.03.11.003 The value 0 MUST indicate that the actual handle cannot open the door locally.


The value 1 MUST indicate that the actual handle can open the door locally.


**Inside** **Door** **Handles** **Mode** **(4** **bits)**

This field is used to advertise the status of each individual inside door handle.


CC:0062.04.03.11.004


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 192




<!-- PAGE 194 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST be treated as a bitmask field and MUST be encoded according to Table 2.202.


CC:0062.04.03.11.005 The value 0 MUST indicate that the actual handle cannot open the door locally.


The value 1 MUST indicate that the actual handle can open the door locally.


**Door** **Condition** **(8** **bits)**

This field is used to advertise the state of the door lock components.

CC:0062.04.03.11.006 This field MUST be encoded according to Table 2.203.



Table 2.203: Door Lock Operation Report::Door Condition bitmask encoding












|Value|Bit 7 3<br>..|Bit 2|Bit 1|Bit 0|
|---|---|---|---|---|
|bit set to ‘0’|_Reserved_|Latch<br>Open<br>(out,<br>engaged,<br>extended)|Bolt Locked (out,<br>extended)|Door Open|
|bit set to ‘1’|_Reserved_|Latch<br>Closed<br>(in,<br>disengaged,<br>retracted)|Bolt<br>Unlocked<br>(in, retracted)|Door Closed|



All other bits are reserved and MUST be set to zero by a sending node. Reserved bits MUST be
ignored by a receiving node.


CC:0062.04.03.11.007 If a door component is not advertised as supported in the Door Lock Capabilities Report Command,
the corresponding bit MUST be set to 0 and MUST be ignored by a controlling node.


**Remaining** **Lock** **Time** **Minutes** **(8** **bits)**

This field is used to advertise the remaining time before the door lock mode will automatically be
changed to “secured” if operating in timed operation with a timed operation mode.

CC:0062.04.03.11.008 This field MUST be encoded according to Table 2.204. The remaining time that the sending node
will stay in the current mode MUST be determined by combining this field and the _Remaining_ _Lock_
_Time_ _Seconds_ field.


Table 2.204: Door Lock Operation Report::Remaining Lock Time
Minutes encoding

|Value|Description|
|---|---|
|0..253 (0x00..0xFD)|0..253 minutes (Operation Type and Current mode = Timed Operation)<br>|
|254 (0xFE)|Undefned|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

CC:0062.04.03.11.009 A node currently set in a constant operation type mode MUST set this field to 0xFE. However,
if unsecured with the auto-relock functionality active, it MAY advertise the time remaining before
auto-relock secures the lock again.


**Remaining** **Lock** **Time** **Seconds** **(8** **bits)**

This field is used to advertise the remaining time before the door lock mode will automatically be
changed to “secured” if operating in timed operation with a timed operation mode.

CC:0062.04.03.11.00A This field MUST be encoded according to Table 2.205. The remaining time that the sending node
will stay in the current mode MUST be determined by combining this field and the _Remaining_ _Lock_
_Time_ _Minutes_ field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 193




<!-- PAGE 195 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.205: Door Lock Operation Report::Remaining Lock Time
Seconds encoding

|Value|Description|
|---|---|
|0..59 (0x00..0x3B)|0..59 seconds (Operation Type and mode= Timed Operation)<br>|
|254 (0xFE)|Undefned|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

CC:0062.04.03.11.00B A node currently set in a constant operation type mode MUST set this field to 0xFE. However,
if unsecured with the auto-relock functionality active, it MAY advertise the time remaining before
auto-relock secures the lock again.


**Target** **Door** **Lock** **Mode** **(8** **bits)**

This field is used to advertise the target mode of an ongoing transition or of the most recent transition.

CC:0062.04.03.11.00C This field MUST be encoded according to Table 2.201. This field MUST be set to the mode specified
in the most-recent received Door Lock Operation Set Command.


CC:0062.04.03.11.00D If the node is going to change mode due to the auto-relock functionality or a timed operation, this
field MUST NOT advertise the future mode and MUST be set to the same value as the _Current_ _Door_
_Lock_ _Mode_ field.

CC:0062.04.03.11.00E If no transition is ongoing, this field MUST be set to the same value as the _Current_ _Door_ _Lock_ _Mode_
field.

CC:0062.04.03.11.00F If the _Current Door Lock Mode_ is set to 0xFE, this field MUST indicate the mode is it going to assume
when the ongoing transition has been completed.


**Duration** **(8** **bits)**

CC:0062.04.03.12.002 This field SHOULD advertise the estimated remaining time before the mode indicated in the _Target_
_Door_ _Lock_ _Mode_ field is reached.

CC:0062.04.03.11.010 This field MUST be set to 0 if the _Target_ _Door_ _Lock_ _Mode_ and _Current_ _Door_ _Lock_ _Mode_ fields are set
to the same value.

CC:0062.04.03.11.011 The encoding of this field MUST be according to Table 2.10.


**2.2.39.6** **Door** **Lock** **Configuration** **Set** **Command**


This command is used to set the configuration of a supporting door lock node.

CC:0062.04.04.11.001 A supporting node MUST be able to operate with the factory default configuration.


Table 2.206: Door Lock Configuration Set Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_CONFIGURATION_SET (0x04)|Command = DOOR_LOCK_CONFIGURATION_SET (0x04)|Command = DOOR_LOCK_CONFIGURATION_SET (0x04)|Command = DOOR_LOCK_CONFIGURATION_SET (0x04)|Command = DOOR_LOCK_CONFIGURATION_SET (0x04)|Command = DOOR_LOCK_CONFIGURATION_SET (0x04)|Command = DOOR_LOCK_CONFIGURATION_SET (0x04)|Command = DOOR_LOCK_CONFIGURATION_SET (0x04)|
|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|
|Outside Door Handles Enabled|Outside Door Handles Enabled|Outside Door Handles Enabled|Outside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|
|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|
|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|
|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|
|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|
|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|
|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|BTB|TA|



**Operation** **Type** **(1** **byte)**


CC:0062.04.04.11.002


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 194




<!-- PAGE 196 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to set the operation type at the supporting node. This field MUST be encoded
according to Table 2.207.


Table 2.207: Door Lock Configuration Set::Operation Type encod
|Table 2. ing Value|.207: Door Lock Configuration Set::Operation Type Description|e encod- Version|
|---|---|---|
|Value|Description|Version|
|0x01|Constant operation|1|
|0x02|Timed operation|1|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

If this field is set to timed operation (0x02), the _Lock_ _Timeout_ _Minutes_ and _Lock_ _Timeout_ _Seconds_
CC:0062.04.04.11.003 fields MUST be set to values different than 0xFE.

CC:0062.04.04.11.004 A supporting node MUST ignore this field if it is set to an operation type that is not advertised as
supported in the Door Lock Capabilities Report Command.


**Outside** **Door** **Handles** **Enabled** **(4** **bits)**

CC:0062.04.04.11.005 This field is used to enable or disable each individual outside door handle at the supporting node.
This field MUST be treated as a bitmask and MUST be encoded according to Table 2.202.


CC:0062.04.04.11.006 The value 0 MUST indicate that the actual handle cannot open the door locally.


The value 1 MUST indicate that the actual handle can open the door locally.


CC:0062.04.04.11.007 A supporting node MUST ignore an outside door handle mode value if it advertises no support for
the corresponding handle in the Door Lock Capabilities Report Command.


**Inside** **Door** **Handles** **Enabled** **(4** **bits)**

CC:0062.04.04.11.008 This field is used to enable or disable each individual inside door handle at the supporting node. This
field MUST be treated as a bitmask and MUST be encoded according to Table 2.202.


CC:0062.04.04.11.009 The value 0 MUST indicate that the actual handle cannot open the door locally.


The value 1 MUST indicate that the actual handle can open the door locally.


CC:0062.04.04.11.00A A supporting node MUST ignore an inside door handle mode value if it advertises no support for the
corresponding handle in the Door Lock Capabilities Report Command.


**Lock** **Timeout** **Minutes** **(8** **bits)**

This field is used to specify the time that the supporting node must wait before returning to the
secured mode when receiving timed operation modes in a Door Lock Operation Set Command.


CC:0062.04.04.11.00B Values in the range 0x00..0xFD MUST indicate the actual number of minutes.

The value 0xFE MUST indicate that this field is undefined.

CC:0062.04.04.11.00C This field MUST be set to 0xFE if the _Operation_ _Type_ field is set to 0x01 (constant operation)

This field MUST be in the range 0x00..0xFD if the _Operation Type_ field is set to 0x02 (timed operation)


CC:0062.04.04.11.00D
The time to stay unlocked MUST be determined by combining this field and the Lock Timeout Seconds
fields.

CC:0062.04.04.11.00E A supporting node MUST ignore this field if it is set to the timed operation type is not advertised as
supported in the Door Lock Capabilities Report Command.


**Lock** **Timeout** **Seconds** **(8** **bits)**

This field is used to specify the time that the supporting node must wait before returning to the
secured mode when receiving timed operation modes in a Door Lock Operation Set Command.


CC:0062.04.04.11.00F Values in the range 0x00..0x3B MUST indicate the actual number of seconds.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 195




<!-- PAGE 197 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value 0xFE MUST indicate that this field is undefined.

CC:0062.04.04.11.010 This field MUST be set to 0xFE if the _Operation_ _Type_ field is set to 0x01 (constant operation)

This field MUST be in the range 0x00..0x3B if the _Operation Type_ field is set to 0x02 (timed operation)

CC:0062.04.04.11.011 The time to stay unlocked MUST be determined by combining this field and the _Lock Timeout Minutes_
field.

CC:0062.04.04.11.012 A supporting node MUST ignore this field if it is set to the timed operation type is not advertised as
supported in the Door Lock Capabilities Report Command.


**Auto-relock** **time** **(16** **bits)**

This field is used to specify the time setting in seconds for auto-relock functionality.

CC:0062.04.04.11.013 This field MUST be ignored by a node advertising no support for the auto-relock functionality in the
Door Lock Capabilities Report Command.


CC:0062.04.04.11.014 The value 0 MUST indicate that the auto-relock functionality is disabled and the door lock MUST
NOT return to secured mode automatically. (unless using Timed Operation)


CC:0062.04.04.11.015 Values in the range 1..65535 MUST indicate that the auto-relock functionality is enabled and the
supporting node MUST return to secured mode after the time in seconds indicated by this field.


**Hold** **and** **release** **time** **(16** **bits)**

This field is used to specify the time setting in seconds for letting the latch retracted after the
supporting node’s mode has been changed to unsecured.

CC:0062.04.04.11.016 This field MUST be ignored by a node advertising no support for the hold and release functionality
in the Door Lock Capabilities Report Command.


CC:0062.04.04.11.017 The value 0 MUST indicate that the hold and release functionality is disabled and the supporting
node MUST NOT keep the latch retracted when the door lock mode becomes unsecured.


CC:0062.04.04.11.018 Values in the range 1..65535 MUST indicate that the hold and release functionality is enabled and
the door lock latch MUST keep open according to the time in seconds indicated by this field.


**TA** **(Twist** **assist)** **(1** **bit)**

CC:0062.04.04.11.019 This field MUST indicate if the twist assist functionality is enabled.

CC:0062.04.04.11.01A This field MUST be ignored by a node advertising no support for the twist assist functionality in the
Door Lock Capabilities Report Command.


CC:0062.04.04.11.01B The value 0 MUST indicate that the twist assist functionality MUST be disabled at the supporting
node.


The value 1 MUST indicate that the twist assist functionality MUST be enabled at the supporting
node.


**BTB** **(Block-to-block)** **(1** **bit)**

This field is used to indicate if the block-to-block functionality is enabled.

CC:0062.04.04.11.01C This field MUST be ignored by a node advertising no support for the block-to-block functionality in
the Door Lock Capabilities Report Command.


CC:0062.04.04.11.01D The value 0 MUST indicate that the block-to-block functionality is disabled and the supporting node
MAY ignore Door Lock Operation Set Commands if it detects to be already in the specified mode.


CC:0062.04.04.11.01E The value 1 MUST indicate that the block-to-block functionality is enabled and the supporting node
MUST activate its motors until blocked to try to reach the mode indicated by Door Lock Operation
Set Commands, even if it detects to be already in the specified mode.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 196




<!-- PAGE 198 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.39.7** **Door** **Lock** **Configuration** **Get** **Command**


This command is used to request the configuration parameters of a door lock device.

CC:0062.04.05.11.001 The Door Lock Configuration Report Command MUST be returned in response to this command.


CC:0062.04.05.51.001 This command MUST NOT be issued via multicast addressing.


CC:0062.04.05.11.002 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.208: Door Lock Configuration Get Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_CONFIGURATION_GET (0x05)|Command = DOOR_LOCK_CONFIGURATION_GET (0x05)|Command = DOOR_LOCK_CONFIGURATION_GET (0x05)|Command = DOOR_LOCK_CONFIGURATION_GET (0x05)|Command = DOOR_LOCK_CONFIGURATION_GET (0x05)|Command = DOOR_LOCK_CONFIGURATION_GET (0x05)|Command = DOOR_LOCK_CONFIGURATION_GET (0x05)|Command = DOOR_LOCK_CONFIGURATION_GET (0x05)|



**2.2.39.8** **Door** **Lock** **Configuration** **Report** **Command**


This command is used to advertise the configuration parameters of a door lock device.


Table 2.209: Door Lock Configuration Report Command, version

|7|Table 2.20 4 6|09: Door Lo 5|ock Configur 4|ration Repo 3|ort Comman 2|nd, version 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_CONFIGURATION_REPORT (0x06)|Command = DOOR_LOCK_CONFIGURATION_REPORT (0x06)|Command = DOOR_LOCK_CONFIGURATION_REPORT (0x06)|Command = DOOR_LOCK_CONFIGURATION_REPORT (0x06)|Command = DOOR_LOCK_CONFIGURATION_REPORT (0x06)|Command = DOOR_LOCK_CONFIGURATION_REPORT (0x06)|Command = DOOR_LOCK_CONFIGURATION_REPORT (0x06)|Command = DOOR_LOCK_CONFIGURATION_REPORT (0x06)|
|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|Operation Type|
|Outside Door Handles Enabled|Outside Door Handles Enabled|Outside Door Handles Enabled|Outside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|Inside Door Handles Enabled|
|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|Lock Timeout Minutes|
|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|Lock Timeout Seconds|
|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|Auto-relock time 1 (MSB)|
|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|Auto-relock time 2 (LSB)|
|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|Hold and release time 1 (MSB)|
|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|Hold and release time 2 (LSB)|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|BTB|TA|



Fields not described below MUST be according to descriptions in Section 2.2.39.6 _Door_ _Lock_ _Config-_
_uration_ _Set_ _Command_ .


**Outside** **Door** **Handles** **Enabled** **(4** **bits)**

This field is used advertise if each individual outside door handle is enabled at the supporting node.
This field MUST be treated as a bitmask and MUST be encoded according to Table 2.202.


**Inside** **Door** **Handles** **Enabled** **(4** **bits)**

This field is used advertise if each individual inside door handle is enabled at the supporting node.
This field MUST be treated as a bitmask and MUST be encoded according to Table 2.202.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 197




<!-- PAGE 199 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.39.9** **Door** **Lock** **Capabilities** **Get** **Command**


This command is used to request the Door Lock capabilities of a supporting node.


CC:0062.04.07.11.001 The Door Lock Capabilities Report Command MUST be returned in response to this command.


CC:0062.04.07.51.001 This command MUST NOT be issued via multicast addressing.


CC:0062.04.07.11.002 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.210: Door Lock Capabilities Get Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_CAPABILITIES_GET (0x07)|Command = DOOR_LOCK_CAPABILITIES_GET (0x07)|Command = DOOR_LOCK_CAPABILITIES_GET (0x07)|Command = DOOR_LOCK_CAPABILITIES_GET (0x07)|Command = DOOR_LOCK_CAPABILITIES_GET (0x07)|Command = DOOR_LOCK_CAPABILITIES_GET (0x07)|Command = DOOR_LOCK_CAPABILITIES_GET (0x07)|Command = DOOR_LOCK_CAPABILITIES_GET (0x07)|



**2.2.39.10** **Door** **Lock** **Capabilities** **Report** **Command**


This command is used to advertise the Door Lock capabilities supported by the sending node.


Table 2.211: Door Lock Capabilities Report Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|Command Class = COMMAND_CLASS_DOOR_LOCK (0x62)|
|Command = DOOR_LOCK_CAPABILITIES_REPORT (0x08)|Command = DOOR_LOCK_CAPABILITIES_REPORT (0x08)|Command = DOOR_LOCK_CAPABILITIES_REPORT (0x08)|Command = DOOR_LOCK_CAPABILITIES_REPORT (0x08)|Command = DOOR_LOCK_CAPABILITIES_REPORT (0x08)|Command = DOOR_LOCK_CAPABILITIES_REPORT (0x08)|Command = DOOR_LOCK_CAPABILITIES_REPORT (0x08)|Command = DOOR_LOCK_CAPABILITIES_REPORT (0x08)|
|Reserved|Reserved|Reserved|Supported Operation type Bit Mask Length|Supported Operation type Bit Mask Length|Supported Operation type Bit Mask Length|Supported Operation type Bit Mask Length|Supported Operation type Bit Mask Length|
|Supported Operation Type Bit Mask 1|Supported Operation Type Bit Mask 1|Supported Operation Type Bit Mask 1|Supported Operation Type Bit Mask 1|Supported Operation Type Bit Mask 1|Supported Operation Type Bit Mask 1|Supported Operation Type Bit Mask 1|Supported Operation Type Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Supported Operation Type Bit Mask N|Supported Operation Type Bit Mask N|Supported Operation Type Bit Mask N|Supported Operation Type Bit Mask N|Supported Operation Type Bit Mask N|Supported Operation Type Bit Mask N|Supported Operation Type Bit Mask N|Supported Operation Type Bit Mask N|
|Supported Door Lock Mode List Length|Supported Door Lock Mode List Length|Supported Door Lock Mode List Length|Supported Door Lock Mode List Length|Supported Door Lock Mode List Length|Supported Door Lock Mode List Length|Supported Door Lock Mode List Length|Supported Door Lock Mode List Length|
|Supported Door Lock Mode 1|Supported Door Lock Mode 1|Supported Door Lock Mode 1|Supported Door Lock Mode 1|Supported Door Lock Mode 1|Supported Door Lock Mode 1|Supported Door Lock Mode 1|Supported Door Lock Mode 1|
|…|…|…|…|…|…|…|…|
|Supported Door Lock Mode M|Supported Door Lock Mode M|Supported Door Lock Mode M|Supported Door Lock Mode M|Supported Door Lock Mode M|Supported Door Lock Mode M|Supported Door Lock Mode M|Supported Door Lock Mode M|
|Supported Outside Handle Modes Bitmask|Supported Outside Handle Modes Bitmask|Supported Outside Handle Modes Bitmask|Supported Outside Handle Modes Bitmask|Supported Inside Handle Modes Bitmask|Supported Inside Handle Modes Bitmask|Supported Inside Handle Modes Bitmask|Supported Inside Handle Modes Bitmask|
|Supported door components|Supported door components|Supported door components|Supported door components|Supported door components|Supported door components|Supported door components|Supported door components|
|Reserved|Reserved|Reserved|Reserved|ARS|HRS|TAS|BTBS|



**Reserved**

CC:0062.04.08.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Supported** **Operation** **Type** **Bit** **Mask** **Length** **(5** **bits)**

This field is used to advertise the length in bytes of the _Supported_ _Operation_ _Type_ _Bit_ _Mask_ field
carried in the command.

CC:0062.04.08.11.002 This field MUST be set to the minimum value which allows to advertise all supported Operation
types.


**Supported** **Operation** **Type** **Bit** **Mask** **(N** **bytes)**

CC:0062.04.08.11.003 This field is used to advertise the supported Door Lock Operation Types values. The length of this
field in bytes MUST match the value advertised in the Supported Operation Type Bit Mask Length
field.

CC:0062.04.08.11.004 This field MUST be encoded as follows:


      - Bit 0 in Bit Mask 1 represents Operation Type 0x00 (Reserved)


      - Bit 1 in Bit Mask 1 represents Operation Type 0x01 (Constant operation)


      - Bit 2 in Bit Mask 1 represents Operation Type 0x02 (Timed operation)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 198




<!-- PAGE 200 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


      - …

Valid Operation Type values are defined in Table 2.207.


CC:0062.04.08.11.005 If an Operation Type is supported, the corresponding bit MUST be set to ‘1’.


If an Operation Type is not supported, the corresponding bit MUST be set to ‘0’.


CC:0062.04.08.11.006 All other bits are reserved and MUST be set to zero by a sending node. Reserved bits MUST be
ignored by a receiving node.


CC:0062.04.08.11.007 A node MUST support the constant operation type 0x01.


**Supported** **Door** **Lock** **Mode** **List** **Length** **(8** **bits)**

CC:0062.04.08.11.008 This field MUST advertise the length in bytes of the _Supported_ _Door_ _Lock_ _Mode_ field carried in the
command.


**Supported** **Door** **Lock** **Mode** **(M** **bytes)**

This field is used to advertise the supported Door Lock Modes values. The length of this field in bytes
CC:0062.04.08.11.009 MUST match the value advertised in the _Supported_ _Door_ _Lock_ _Mode_ _List_ Length field.

CC:0062.04.08.11.00A Each byte MUST indicate the value of a supported Door Lock Mode that can be specified in a Door
Lock Operation Set Command. Each byte MUST be encoded according to Table 2.198.


CC:0062.04.08.11.00B A sending node MUST advertise support for the Door Lock modes 0x00 and 0xFF.


**Supported** **Outside** **Handle** **Modes** **Bitmask** **(4** **bits)**

This field is used to advertise which outside handles can be enabled and disabled using the Door Lock
Configuration Set Command.

CC:0062.04.08.11.00C This field MUST be treated as a bitmask and represent outside door handles as described in Table
2.202.


CC:0062.04.08.11.00D If the corresponding handle can be enabled and disabled, the corresponding bit MUST be set to 1.


If the corresponding handle cannot be enabled or disabled, the corresponding bit MUST be set to 0.


**Supported** **Inside** **Handle** **Modes** **Bitmask** **(4** **bits)**

This field is used to advertise which inside handles can be enabled and disabled using the Door Lock
Configuration Set Command.

CC:0062.04.08.11.00E This field MUST be treated as a bitmask and represent inside door handles as described in Table
2.202.


CC:0062.04.08.11.00F If the corresponding handle can be enabled, the corresponding bit MUST be set to 1.


If the corresponding handle cannot be enabled, the corresponding bit MUST be set to 0.


**Supported** **Door** **components** **(8** **bits)**


CC:0062.04.08.11.010
This field MUST advertise the supported door lock component that can be reported in the Door Lock
condition field of the Door Lock Operation Report Command.

CC:0062.04.08.11.011 This field MUST be treated as a bitmask and represent inside door handles as described in Table
2.212.


Table 2.212: Door Lock Capabilities Report::Supported Door com
|Table 2. ponents Bit 7..3|.212: Door Lock Capabilit encoding Bit 2|ties Report::Supported Do Bit 1|oor com- Bit 0|
|---|---|---|---|
|Bit 7..3|Bit 2|Bit 1|Bit 0|
|_Reserved_|Latch|Bolt|Door|



CC:0062.04.08.11.012 If the corresponding component is supported, the corresponding bit MUST be set to ‘1’.


If the corresponding component is not supported, the corresponding bit MUST be set to ‘0’.


**ARS** **(Auto-Relock** **support)** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 199




<!-- PAGE 201 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to advertise if the sending node supports the auto-relock functionality.


CC:0062.04.08.11.013 The value 1 MUST indicate that the auto-relock functionality is supported.


The value 0 MUST indicate that the auto-relock functionality is not supported.


**HRS** **(Hold** **and** **release** **support)** **(1** **bit)**

CC:0062.04.08.11.014 This field MUST advertise if the hold and release functionality is supported.


CC:0062.04.08.11.015 The value 0 MUST indicate that the hold and release functionality is not supported


The value 1 MUST indicate that the hold and release functionality is supported.


**TAS** **(Twist** **assist** **support)** **(1** **bit)**

CC:0062.04.08.11.016 This field MUST advertise if the Twist Assist functionality is supported.


CC:0062.04.08.11.017 The value 0 MUST indicate that the twist assist functionality is not supported


The value 1 MUST indicate that the twist assist functionality is supported.


**BTBS** **(Block-to-block** **support)** **(1** **bit)**

This field is used to advertise if the block-to-block functionality is supported.


CC:0062.04.08.11.018 The value 0 MUST indicate that the block-to-block functionality is not supported


The value 1 MUST indicate that the block-to-block functionality is supported.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 200