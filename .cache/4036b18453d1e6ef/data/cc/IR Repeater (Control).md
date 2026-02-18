<!-- PAGE 1106 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.10** **IR** **Repeater** **Command** **Class,** **version** **1**


**6.2.10.1** **Mandatory** **node** **interview**


CL:00A0.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.10.


Figure 6.10: IR Repeater Command Class interview


**6.2.10.2** **Minimum** **end** **user** **functionalities**


CL:00A0.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.10.2.1** **Repeat** **an** **IR** **code**


CL:00A0.01.31.02.1 This action MUST be available to the end user if the supporting node supports repeating IR Codes.


CL:00A0.01.31.03.1 When the end user performs this action, the issued commands MUST comply with Table 6.15.

|Field|Table 6.15: IR Repeater::Repeat an IR Code Value|
|---|---|
|Field|Value|
|Command|IR_REPEATER_REPEAT<br>|
|Sequence number|Controlling node defned. It MUST be incremented at each new repeat<br>action<br>|
|Sub carrier|Controlling node defned within the capabilities of the supporting node<br>|
|Duty Cycle|Controlling node defned within the capabilities of the supporting node<br>|
|Pulse time unit|Controlling node defned within the range advertised by the supporting<br>node in the IR Repeater Capabilities Report Command<br>|
|Report Number|Controlling node defned.|
|Last|1 for the last command, 0 else.<br>|
|Data|Controlling node defned.<br>The end user MUST be able to select an IR Code that will be transferred.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1105




<!-- PAGE 1107 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.10.2.2** **Learn** **an** **IR** **code**


CL:00A0.01.31.04.1 This action MUST be available to the end user if the supporting node supports Learning IR Codes.


CL:00A0.01.31.04.1 When the end user performs this action, the issued command MUST comply with Table 6.16.

|Field|Table 6.16: IR Repeater::Learn an IR Code Value|
|---|---|
|Field|Value|
|Command<br>|IR_REPEATER_IR_CODE_LEARNING_START<br>|
|IR Code identifer|User defned among available IR Codes slots<br>|
|Timeout|Controlling node or User defned.<br>|
|Pulse time unit|Controlling node defned within the range advertised by the supporting<br>node in the IR Repeater Capabilities Report Command|



The Controlling node MUST inform the user about the status of the IR Code learning when the IR
Code Learning Status Command is received.


The controlling node MAY allow the end user to interrupt the learning process, if it does, the issued
command MUST comply with Table 6.17.


Table 6.17: IR Repeater::Stop learning an IR code

|Field|Value|
|---|---|
|Command|IR_REPEATER_IR_CODE_LEARNING_STOP|



**6.2.10.2.3** **Erase** **a** **learnt** **IR** **code**


CL:00A0.01.31.05.1 This action MUST be available to the end user if the supporting node supports Learning IR Codes.


CL:00A0.01.31.06.1 When the end user performs this action, the issued command MUST comply with Table 6.18.


Table 6.18: IR Repeater::Erase an IR Code from memory

|Field|Value|
|---|---|
|Command<br>|IR_REPEATER_LEARNT_IR_CODE_REMOVE<br>|
|IR Code identifer|User defned among available IR Codes slots that have a defned IR Code|



**6.2.10.2.4** **Repeat** **a** **learnt** **IR** **code**


CL:00A0.01.31.07.1 This action MUST be available to the end user if the supporting node supports Repeating IR Codes.


CL:00A0.01.31.08.1 When the end user performs this action, the issued command MUST comply with Table 6.19.

|Field|Table 6.19: IR Repeater::Repeat a learnt IR code Value|
|---|---|
|Field|Value|
|Command<br>|IR_REPEATER_REPEAT_LEARNT_CODE<br>|
|IR Code identifer|User defned among available Learnt IR Codes slots|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1106




<!-- PAGE 1108 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.10.3** **Node** **properties**


If the supporting node supports IR Code learning:

CL:00A0.01.41.01.1 - A controlling node MUST have a UI allowing the end user to see the which IR Code Identifiers
contain a valid learnt code.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1107




<!-- PAGE 1109 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.11** **Meter** **Command** **Class,** **version** **1-5**


**6.2.11.1** **Mandatory** **node** **interview**


CL:0032.01.21.01.2 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.11.


Figure 6.11: Meter Command Class interview


**6.2.11.2** **Minimum** **end** **user** **functionalities**


CL:0032.02.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.11.2.1** **Reset** **cumulated** **data**


CL:0032.02.31.02.1 This action MUST be available to the end user if both nodes implement version 2 or newer and the
supporting node indicates that meter reset is supported.


CL:0032.02.31.03.1 When the end user performs this action, the issued command MUST comply with Table 6.20.

|Field|Table 6.20: Meter::Reset cumulated data Value|
|---|---|
|Field|Value|
|Command (v2)|METER_RESET|



**6.2.11.3** **Node** **properties**


CL:0032.01.41.01.2 A controlling node MUST have a UI allowing the end user to see the last readings for each supported
scale and all cumulated values. For version 1 supporting nodes, the scale reported in the Meter Report
MUST be accessible to the end user.


CL:0032.01.41.02.1 A controlling node MUST always show the value even if the Type and/or Scale are unknown.


CL:0032.01.42.01.1 A controlling node SHOULD implement the capability to update its list of Meter Type and Scales,
so that new Meter Types and scales added in more recent versions are not presented as unknown.


CL:0032.01.41.03.1 If a controlling node receives an unknown Meter Type or Scale, it MUST allow the end user to identify
the Meter reading and MAY allow the user to assign a free-text description to that Meter reading


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1108




<!-- PAGE 1110 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.11.4** **Additional** **control** **requirements**


CL:0032.01.51.01.1 Unless unsolicited Meter Report Commands are received, a controlling node MUST:


     - Probe the current meter readings for each supported scale (and rate type if v4 nodes) at least
every 6 hours for listening nodes.


     - Probe the current meter readings for each supported scale (and rate type if v4 nodes) when the
supporting node issues a Wake Up Notification Command for sleeping nodes.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1109




<!-- PAGE 1111 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.12** **Multilevel** **Sensor** **Command** **Class,** **version** **1-11**


**6.2.12.1** **Mandatory** **node** **interview**


CL:0031.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.12.


Figure 6.12: Multilevel Sensor Command Class interview


**6.2.12.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.2.12.3** **Node** **properties**


CL:0031.01.41.01.1 A controlling node MUST allow the end user to see the received readings for every Sensor types


CL:0031.01.41.02.1 A controlling node MUST always show the sensor reading values even if the Sensor Type and/or Scale
are unknown.


CL:0031.01.42.01.1 A controlling node SHOULD implement the capability to update its list of Sensor Type and Scales,
so that new Sensor Types and Scales added in [27] are not presented as unknown.


CL:0031.01.41.03.2 If a controlling node receives an unknown Sensor Type or Scale, it MUST allow the end user to identify
the Sensor reading and MAY allow the end user to assign a free-text description to the sensor reading.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1110




<!-- PAGE 1112 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.12.4** **Additional** **control** **requirements**


CL:0031.01.51.01.1 Unless unsolicited Multilevel Sensor Report Commands are received, a controlling node MUST:


     - Probe the current reading for each supported sensor type at least every 6 hours for listening
nodes.


     - Probe the current reading for each supported sensor type when the supporting node issues a
Wake Up Notification Command for sleeping nodes.


CL:0031.01.52.01.1 A node controlling this command class SHOULD also control:


     - Association Command Class, version 2


     - Association Group Information, version 3


CL:0031.01.52.02.1 A controlling node SHOULD associate itself to an association group issuing Multilevel Report Commands after performing a supporting node interview and providing end user functionalities.


CL:0031.01.51.02.1 A controlling node MUST NOT remove associations in order to associate itself to an association group
issuing Multilevel Report Commands.

CL:0031.01.52.03.1 Controller SHOULD have a UI allowing the end user to define rules or commands based on received
readings.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1111




<!-- PAGE 1113 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.13** **Multilevel** **Switch** **Command** **Class,** **version** **1-4**


**6.2.13.1** **Mandatory** **node** **interview**


CL:0026.01.21.01.2 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.13. It is OPTIONAL to issue the _Multilevel_ _Switch_ _Supported_ _Get_ _Command_ if a controlling
node does not use this information for its UI.


Figure 6.13: Multilevel Switch Command Class interview


**6.2.13.2** **Mimimum** **End** **User** **Functionalities**


CL:0026.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.13.2.1** **Set** **the** **Level**


CL:0026.01.31.02.2 When the end user performs this action, the issued command MUST comply with Table 6.21.

|Field|Table 6.21: Multilevel Switch::Set the level Value|
|---|---|
|Field|Value|
|Command|SWITCH_MULTILEVEL_SET<br>|
|Value|User defned among 0x00..0x63. Using 0xFF is optional.<br>|
|Duration (v2)|User defned or 0xFF|



**6.2.13.3** **Node** **Properties**


CL:0026.01.42.01.1 Controller SHOULD have a UI allowing the end user to see the following properties:


     - Last known state (xx%)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1112




<!-- PAGE 1114 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.14** **Notification** **Command** **Class,** **version** **1-8**


**6.2.14.1** **Mandatory** **Node** **Interview**


CL:0071.02.21.01.2 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.14.


Figure 6.14: Notification Command Class interview


CL:0071.02.23.01.1 The step denoted as “1. Read Notification Type Status” in Figure 6.14 MAY be replaced by Notification Set commands for each Notification Type, with the Status field set to 0x00 or 0xFF.


CL:0071.02.23.02.1 A node controlling this command class MAY skip the AGI Interview (refer to Section 6.3.2) if the
supporting node is a Z-Wave Plus node and the controlling node has estalished a Lifeline Association.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1113




<!-- PAGE 1115 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.14.2** **Minimum** **End** **User** **Functionalities**


No minimum end user functionality is required for this Command Class.


**6.2.14.3** **Node** **Properties**


CL:0071.01.41.01.1 A controlling node MUST have a UI allowing the end user to see the received Notification Reports
(Notification type and event/state).


**6.2.14.4** **Additional** **Control** **Requirements**


CL:0071.01.51.01.1 A controlling node MUST probe state/event notifications from pull nodes


     - at least every 6 hours for listenting nodes.

     - when the supporting node issues a Wake up Notification Command for sleeping nodes.


CL:0071.01.51.02.1 A node controlling this command class MUST also control:


     - Association Command Class, version 2


     - Association Group Information, version 3

CL:0071.01.51.03.1 For Push supporting nodes, a controlling node MUST associate itself to a group issuing Notification
Report Commands before performing a supporting node interview and providing end user functionalities.


CL:0071.01.53.01.1 For Push supporting nodes, it is OPTIONAL for a controlling node to provide end user functionalities
and node properties if it cannot associate itself to an association group sending Notification Report
Commands. (e.g. all Association Groups sending the relevant command are full)


CL:0071.01.51.04.1 A controlling node MUST NOT remove associations in order to associate itself to an association group
issuing Notification Report Commands.

CL:0071.01.52.01.1 Controller SHOULD have a UI allowing the end user to define rules or commands based on received
notifications events/states.

CL:0071.01.52.02.1 A controlling node SHOULD implement the capability to update its Notifications list, so that new
Notifications added in [36] are not presented as unknown.

CL:0071.01.51.05.2 If a controlling node receives an unknown Notification, it MUST allow the end user to identify this
notification and MAY allow the end user to assign a free-text description to that Notification.


**6.2.14.4.1** **Detailed** **Controller** **Guidelines**


This section presents guidelines for controlling legacy sensors nodes supporting the Notification Command Class, version 3-8.


Alarm Command Class version 2 supporting nodes operate in Push mode only. The guidelines presented in Section 6.2.14.4.7 Controlling Pull Mode Sensors can also be used for controlling Alarm CC
version 2 supporting nodes.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1114




<!-- PAGE 1116 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.14.4.2** **Sensor** **database**


The following sections present discovery methods for sensor properties, such as Push/Pull mode or
the use of state idle notifications. Some sensor properties (e.g. configuration parameters, Association
group properties, state variables dependencies) cannot always be discovered.

CL:0071.01.52.03.1 If a controlling node has a database of known certified Notification sensors, it SHOULD be consulted
first before attempting to interview the Notification Command Class of a supporting node. If the
supporting node is present in the database, a controlling node SHOULD read the sensor properties
from the database and skip any discovery.


**6.2.14.4.3** **Push/Pull** **mode** **discovery**


A supporting node does not advertise whether it operates in Push or Pull mode. Therefore a controlling
CL:0071.01.51.06.1 node MUST discover what mode a supporting node implements.


CL:0071.01.52.04.1 The RECOMMENDED discovery steps for a controlling node are the following:


If the supporting node does not support the Association Command Class, it may be concluded that
the supporting node implements Pull Mode and discovery may be aborted.


If the supporting node supports the AGI Command Class, probe the AGI table in the following way
or read the already probed AGI table:


1. Discover how many Association groups the supporting node (and its eventual End Points) implements by issuing an Association Supported Groupings Get Command.


2. For each association group, issue an Association Group Command List Get for the grouping identifier. Inspect the returned Association Group Command List Report and look for the following
pair: {Command Class x = COMMAND_CLASS_NOTIFICATION, Command x = NOTIFICATION_REPORT}. If a match is found, conclude that the supporting node implements Push
Mode and stop the discovery process.


If no match is found at the end of the AGI test, conclude that the supporting node implements Pull
Mode. The AGI test is illustrated in Figure 6.15.


Figure 6.15: Push/Pull Node Discovery, AGI table probing


If the supporting node does not support the AGI Command Class, proceed with the following Notification Command Class test:

1. Discover the list of supported Notification Types by issuing a Notification Supported Get Command.

2. For each supported Notification Type, query the supported Events/States via the Event Supported Get Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1115




<!-- PAGE 1117 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


3. Set the status of one of the Supported Notification Types at the target node using a Notification
Set Command with the following values:

a. Notification Type = (a supported type discovered in step 1)

b. Notification Status = 0xFF

4. Issue a Notification Get Command with the following values:

a. Notification Type = (Same as step 3.a).

b. Notification Event = (a supported Event/State discovered in step 2).

5. The supporting node returns a Notification Report Command.

a. If the Notification Status is 0xFF, the target node implements Push Mode

b. If the Notification Status is 0xFE or 0x00, the target node implements Pull Mode


c. If the target node did not return a report within 10 seconds, it implements Pull Mode

The Notification Command Class test is illustrated in Figure 6.16.


Figure 6.16: Push/Pull Node Discovery, Notification Command Class test


**6.2.14.4.4** **Unknown** **Notifications**


CL:0071.01.52.05.1 This Command Class defines some Notifications as event or states. It is RECOMMENDED to treat
an unknown Notification as its own state variable.


**6.2.14.4.5** **State** **idle**


A controlling node receiving a “State idle” Notification for an event or state of which the “State idle”
CL:0071.01.52.06.1 Notification does not apply (e.g. the “heartbeat” event) SHOULD ignore the Notification. Refer to

[36] for state variables to which the “State idle” notification applies.



CL:0071.01.52.07.2


CL:0071.01.53.02.1



It is not mandatory for nodes supporting Notification Command Class, version 7 or older to send a
“State idle” Notification for returning a state variable to idle. Thus, there is a risk that a “State idle”
is never sent. A controlling node SHOULD NOT use timeouts to consider a state variable to be idle
for example 5 minutes after the last received Notification for v8 or newer supporting nodes. It MAY
allow the end user to mark states variables as idle.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1116




<!-- PAGE 1118 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.14.4.6** **Parameter** **encapsulation**


CL:0071.01.53.03.1 A node implementing version 5 or older MAY use the following parameter encapsulation format: (User
ID, User Code Report Command) instead of (User Code Report Command).


CL:0071.01.52.08.1 A controlling node SHOULD accept the end user Code Report Event Parameter with a User ID byte
prefixed at the beginning of the Notification Event Parameter for backwards compatibility. A controlling node can detect the beginning of the end user Code Report by finding the following consecutive
bytes: {byte x= COMMAND_CLASS_USER_CODE, byte x+1 = USER_CODE_REPORT}.


**6.2.14.4.7** **Controlling** **Pull** **Mode** **Sensors**


The following sections present guidelines for controlling Pull sensors nodes.


**6.2.14.4.8** **Notification** **Get** **Command**


This command is used to retrieve the next Notification from the receiving node’s queue. Below are
recommendations for what values controlling nodes should set in the fields of this command.

**Notification** **Type** **(8** **bits)**

CL:0071.01.52.09.1 A controlling node SHOULD set the Notification Type field to 0xFF.

Earlier specification text suggested that Pull nodes must not ignore this command if the Notification
Type is set to a supported type; rather than 0xFF. Therefore, Pull sensors may respond to a Notification Get for a supported Notification type by retrieving the next notification in the queue matching
the specified Notification Type.

**Notification** **Event** **/State** **(8** **bits)**

CL:0071.01.52.0A.1 A controlling node SHOULD set this field to 0x00.

A receiving node will have an unpredictable behavior if this field is set to a supported Event.


**6.2.14.4.9** **Detecting** **and** **clearing** **persistent** **notifications**


It is optional for Pull nodes to specify a sequence number in notifications.

CL:0071.01.52.0B.1 A controlling node receiving twice the same Notification with identical sequence number SHOULD
consider the Notification as persistent. An example is given in Figure 6.17.


Figure 6.17: Detecting and Clearing Persistent Notifications, identical sequence numbers


Due to unclear specification text, sensors may issue persistent Notifications without a sequence number
CL:0071.01.52.0C.1 field or with a new sequence number every time. Therefore, a controlling node SHOULD consider


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1117




<!-- PAGE 1119 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


a notification to be persistent if it receives the same Notification (type and event/state) 5 times or
more. An example is given in Figure 6.18.


Figure 6.18: Detecting and clearing persistent notifications with incremental sequence numbers


**6.2.14.4.10** **Status** **and** **queue** **empty**


CL:0071.01.52.0D.1
A controlling node SHOULD stop issuing Notification Get Commands when receiving a Queue empty
notification (0xFE). Illustration is given in Figure 6.19.


CL:0071.01.53.04.1
All fields following the Status field MAY be omitted in the Notification Report if it advertises a Status
of 0xFE (queue empty).


Figure 6.19: Pull node event retrieval until receiving queue empty


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1118




<!-- PAGE 1120 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.15** **Simple** **AV** **Control** **Command** **Class,** **version** **1-4**


**6.2.15.1** **Mandatory** **Node** **interview**


CL:0094.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.20.


Figure 6.20: Simple AV Control Command Class interview


**6.2.15.2** **Minimum** **end** **user** **functionalities**


CL:0094.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.15.2.1** **Send** **a** **supported** **AV** **code**


CL:0094.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.22.


Table 6.22: Simple AV Control::Send a supported AV code

|Field|Value|
|---|---|
|Command|SIMPLE_AV_CONTROL_SET<br>|
|Sequence number|Controlling node defned. This feld MUST be incremented every time<br>the end user perform this action<br>|
|Key attributes|User defned<br>|
|Command x|User defned among supported AV codes|



CL:0094.01.31.03.1 The end user MUST be able to select among all supported AV codes even if the controlling node does
not know what the code actually represents.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1119




<!-- PAGE 1121 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.15.3** **Node** **properties**


CL:0094.01.41.01.1 Controller SHOULD have a UI allowing the end user to see the following properties:


     - List of supported AV Codes


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1120