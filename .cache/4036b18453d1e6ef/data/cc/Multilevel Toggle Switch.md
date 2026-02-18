<!-- PAGE 344 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.73** **Multilevel** **Toggle** **Switch** **Command** **Class,** **version** **1**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **DEPRECATED**


A device MAY implement this command class, but it is RECOMMENDED that new implementations use the Multilevel Switch Command Class.


If implementing this command class, it is RECOMMENDED that the Multilevel Switch Command
Class is also implemented.


The Multilevel Toggle Switch Command Class is used for multilevel toggle-style actuator devices.


**2.2.73.1** **Multilevel** **Toggle** **Switch** **Set** **Command**


This command is used to set the level in a device that supports the multilevel switch functionality.


Table 2.419: Multilevel Toggle Switch Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|
|Command = SWITCH_TOGGLE_MULTILEVEL_SET|Command = SWITCH_TOGGLE_MULTILEVEL_SET|Command = SWITCH_TOGGLE_MULTILEVEL_SET|Command = SWITCH_TOGGLE_MULTILEVEL_SET|Command = SWITCH_TOGGLE_MULTILEVEL_SET|Command = SWITCH_TOGGLE_MULTILEVEL_SET|Command = SWITCH_TOGGLE_MULTILEVEL_SET|Command = SWITCH_TOGGLE_MULTILEVEL_SET|



**2.2.73.2** **Multilevel** **Toggle** **Switch** **Get** **Command**


This command is used to request the state of the load controlled by the device.


The Multilevel Toggle Switch Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.420: Multilevel Toggle Switch Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|
|Command = SWITCH_TOGGLE_MULTILEVEL_GET|Command = SWITCH_TOGGLE_MULTILEVEL_GET|Command = SWITCH_TOGGLE_MULTILEVEL_GET|Command = SWITCH_TOGGLE_MULTILEVEL_GET|Command = SWITCH_TOGGLE_MULTILEVEL_GET|Command = SWITCH_TOGGLE_MULTILEVEL_GET|Command = SWITCH_TOGGLE_MULTILEVEL_GET|Command = SWITCH_TOGGLE_MULTILEVEL_GET|



**2.2.73.3** **Multilevel** **Toggle** **Switch** **Report** **Command**


This command is used to advertise the level of a toggle switch.


Table 2.421: Multilevel Toggle Switch Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|
|Command = SWITCH_TOGGLE_MULTILEVEL_REPORT|Command = SWITCH_TOGGLE_MULTILEVEL_REPORT|Command = SWITCH_TOGGLE_MULTILEVEL_REPORT|Command = SWITCH_TOGGLE_MULTILEVEL_REPORT|Command = SWITCH_TOGGLE_MULTILEVEL_REPORT|Command = SWITCH_TOGGLE_MULTILEVEL_REPORT|Command = SWITCH_TOGGLE_MULTILEVEL_REPORT|Command = SWITCH_TOGGLE_MULTILEVEL_REPORT|
|Value|Value|Value|Value|Value|Value|Value|Value|



**Value** **(8** **bits)**

The value MAY be 0x00 (off/disable) or 0xFF (on/enable).

The field MAY carry values from 1 to 99.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 343




<!-- PAGE 345 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.73.4** **Multilevel** **Toggle** **Switch** **Start** **Level** **Change** **Command**


This command is used to inform a multilevel toggle switch, that it should start changing the level.
The speed that the switch increases or decreases the level with is implementation specific.



Table 2.422: Multilevel Toggle Switch Start Level Change Com








|7|Table mand 6|2.422: Multilevel T 5|Toggle Swit 4|tch Start Le 3|evel Change 2|Com- 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|
|Command = SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_START_LEVEL_CHANGE|
|Roll<br>Over|Re-<br>served|Ignore Start<br>Level|Reserved|Reserved|Reserved|Reserved|Reserved|
|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|Start Level|


**Roll** **Over** **(1** **bit)**


If the Roll Over bit is set to 0, the switch SHOULD stop when reaching the max or min level. If the
roll over bit is set to 1, the switch SHOULD continually increase and decrease the level until otherwise
instructed.


**Ignore** **Start** **Level** **(1** **bit)**

If the Ignore Start Level bit is set to 0 the switch SHOULD use the start level specified in the
Command. If field is set to 1 the switch SHOULD start from the actual level in the device.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Start** **Level** **(8** **bits)**

The Start Level field contains the initial level that the switch should assume when it start to change
the level.


**2.2.73.5** **Multilevel** **Toggle** **Switch** **Stop** **Level** **Change** **Command**


This command is used to inform a multilevel toggle switch, that it should stop changing the level.


Table 2.423: Multilevel Toggle Switch Stop Level Change Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|Command Class = COMMAND_CLASS_SWITCH_TOGGLE_MULTILEVEL|
|Command = SWITCH_TOGGLE_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_STOP_LEVEL_CHANGE|Command = SWITCH_TOGGLE_MULTILEVEL_STOP_LEVEL_CHANGE|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 344




<!-- PAGE 346 -->

CC:0071.03.00.13.001


CC:0071.03.00.12.001


CC:0071.03.00.12.002



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.74** **Notification** **Command** **Class,** **version** **3-8**


**Warning:** **THIS** **COMMAND** **CLASS** **VERSIONS** **3-7** **HAVE** **BEEN** **DEPRECATED**


A device MAY implement version 3 to 7, but it is RECOMMENDED that new implementations
comply with Notification Command Class, version 8


Pull Mode has been deprecated; it is RECOMMENDED that new implementations support Push
Mode


The Notification Command Class is used to advertise events or states, such as movement detection,
door open/close or system failure. The Notification Command Class supersedes the Alarm Command
Class.


**2.2.74.1** **Terminology**


Sensors may be designed for several purposes. A multilevel sensor advertises measurements or readings.
A **notification** **sensor** sends **event** or **state** **notifications** .

This Command Class is used for notification sensors. The Multilevel Sensor Command Class is used
for multilevel sensors.

Notifications are categorized into logical groups called **Notification Types** . A Notification is denoted
with its type and event/state: {Notification Type::event/state}. A node may send Notifications from
several Notification Types.


An event only has a meaning in the moment it happens. An event does not indicate the value of a
state variable. An example is given in Figure 2.14.


Figure 2.14: Event notifications inform only about instantaneous situations


A **state** **variable** may assume two or more states. Some state variables are returned to their idle
state via a generic “State idle” Notification.

For example, a controlling node receiving a {Smoke alarm::Smoke detected} Notification will consider that the state has not changed until it receives a {Smoke alarm::State idle(Smoke detected)}
Notification. An illustration is given in Figure 2.15.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 345




<!-- PAGE 347 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 2.15: Binary state variable with generic “State idle” Notification


The “State idle” notification may also be used to return a multi-value state variable to its idle state.
An example is given in Figure 2.16.


Figure 2.16: Multi-value state variable with generic “State idle” Notification


Some state variables use a specific Notification defined for each state change. Figure 2.17 shows an
example of such a state variable.


Figure 2.17: Binary state variable with specific idle state Notification


Some notifications are complemented with **event/state** parameters. For example, the {System::System software failure} Notification may be accompanied with the manufacturer’s failure/error codes as
event parameters.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 346




<!-- PAGE 348 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Event/state parameters may also affect state variables and their states. For example, the Notification
{Irrigation::Schedule started} takes a 1-byte parameter which identifies the Schedule ID that is started.
In that case, each state variable is identified using the state parameters, thus creating a state variable

array.

An illustration is given in Figure 2.18, where the same Notifications with different parameters advertise
the state of different state variables.


Figure 2.18: State variable array defined by additional Event/State Parameters


A complete list of Notifications (including state variables, event parameters, etc.) is given in [36].

A notification node operates either in **Push** or in **Pull** mode.

A Push node sends **unsolicited** Notifications. The transmission of unsolicited notifications may be
**disabled** or **enabled** . When enabled, unsolicited Notifications are transmitted via an Association
Group. It is not possible to subsequently retrieve Notifications issued by a Push node.

A Pull sensor collects events and state changes in a queue of pending Notifications. Notifications are
retrieved one by one from the Pull sensor queue via the Notification Get Command. The Pull sensor
advertises that its queue is empty when all Notifications have been retrieved.

A persistent Pull Notification is not removed from the Pull sensor queue until it is actively cleared by
a controlling node.


**2.2.74.2** **Compatibility** **considerations**


**2.2.74.2.1** **Notifications** **and** **Command** **Class** **version**


New Notification Types and Notifications have been added to each new version of this Command
CC:0071.03.00.21.001 Class. A node MUST implement as a minimum the Notification Command Class version associated
with the Notifications it sends. The minimum required version for each Notification is specified in

[36].


**2.2.74.2.2** **Push** **mode** **requirements**


CC:0071.03.00.22.001 A node supporting the Notification Command Class SHOULD implement Push mode.


CC:0071.03.00.21.002 A Push node MUST implement the Association Command Class.


CC:0071.03.00.22.002 A Push node SHOULD advertise Association Groups through the Association Group Information
(AGI) Command Class.


CC:0071.03.00.21.003 A Z-Wave Plus Push node MUST:

      - Provide all supported Notifications via the Lifeline Association group.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 347




<!-- PAGE 349 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


      - Advertise Association Groups through the Association Group Information (AGI) Command
Class.


**2.2.74.2.3** **Pull** **mode** **requirements**


Earlier text revisions presented inconsistencies and undefined behaviors for Pull nodes. Thus, existing
CC:0071.03.00.22.003 Pull nodes may behave differently than expected by a controlling node. A node supporting the
Notification Command Class SHOULD NOT implement Pull mode.


CC:0071.03.00.23.001

A Pull node MAY reorder Notifications according to priority so that the first detected event is not the
CC:0071.03.00.22.004 first to be reported. A Pull node SHOULD NOT reorder states of the same state variable in the event
queue. For example, the “Program in progress” and “Program completed” Notifications SHOULD
stay in the same order.

CC:0071.03.00.22.005 A Pull node having its queue full SHOULD remove the oldest notification entry from the queue.

CC:0071.03.00.22.006 Persistent notifications SHOULD carry a sequence number.


**2.2.74.2.4** **Multi** **Channel** **considerations**


CC:0071.03.00.21.004 If several End Points within a Multi Channel device support the Notification Command Class, they
MUST all operate in the same mode (i.e. either all End Points operate in Push mode or all End
Points operate in Pull mode).


**2.2.74.2.5** **Multi** **Channel** **Push** **nodes**


**CC:0071.03.00.2** 31 **.00** 25 While End Points MAY send identical notifications via the Root Device Lifeline Group, the Root
Device MUST NOT send identical Notifications on behalf of multiple End Points. Illustrations are
given in Figure 2.19 and Figure 2.20.


Figure 2.19: Multi Channel device aggregating Notifications (Lifeline group)


Figure 2.20: Multi Channel device with End Point notification overlap (Lifeline group)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 348




<!-- PAGE 350 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A Multi Channel node with identical End Points issuing the same binary state notification with generic
CC:0071.03.00.23.003 state idle Notification MAY be an exception and issue binary Notifications representing the state all
End Points.

CC:0071.03.00.21.008 If doing so, the Root Device MUST issue the active state notification if any of the End Points has the
active binary state and MUST issue the event inactive Notification when all End Points are back to
the “State idle”.


Figure 2.21: Notification representing all End Points for Binary State with generic State Idle notification


CC:0071.03.00.21.006 Z-Wave Plus Multi Channel devices MUST send End Point Push notifications via the Root Device
Lifeline Association Group (if notifications are not identical).


CC:0071.03.00.22.007 A controlling node SHOULD create a Multi Channel Association to the Lifeline group of a supporting
node. Thus Notifications will be sent Multi Channel encapsulated via the Root Device Lifeline group,
allowing End Points to send identical Notifications.

Individual End Point Notifications can be enabled/disabled by sending a Multi Channel encapsulated
Notification Set Command to an End Point, even when End Point Notifications are actually sent via
the Root Device Lifeline group.


**2.2.74.2.6** **State** **idle**


Every Notification Type has the same generic Notification 0x00 “State idle”, (also known as “Event
Inactive” in older specification text) which was introduced in version 4. The Notification allows the
device to advertise that a state variable returned to its idle state.

CC:0071.04.00.23.001 A Push sensor MAY send repeated state Notifications without sending any “State idle” Notification
to indicate that a given state is still active. For instance, a smoke sensor can send a “Smoke Detected”
Notification every five minutes to indicate that the state variable has not returned to idle (refer to
Figure 16.).

Notification Command Class, version 8 increases the requirement level for the use of the “State idle”
CC:0071.08.00.21.001 Notification from OPTIONAL to REQUIRED. Refer to Section 2.2.74.2.12.

CC:0071.04.00.22.001 A supporting node SHOULD NOT send a “State idle” notification for an event or for a state variable
to which state idle does not apply. Refer to [36] for state variables to which the “State idle” notification
applies


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 349




<!-- PAGE 351 -->

CC:0071.03.00.21.007



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.74.2.7** **Version** **3** **[DEPRECATED]**


The Notification Command Class version 3 is an extension of the Alarm Command Class version 2
and adds the following:

 - Additional Notifications (refer to [36])


 - Interview process includes Events (Event Supported Get / Event Supported Report)

 - Sequence field added for collection management of reports

 - The queue empty status (=0xFE) for Pull nodes. A Pull node can now advertise Notification
Status = “no pending notifications”


Commands not mentioned in this version are unchanged from Alarm Command Class version 1 and/or
Alarm Command Class version 2.

The CC identifier for Notification CC V3 is the same as the Alarm CC V1 and V2. However, the
Notification Command Class is not fully backwards compatible with the Alarm Command Class,
versions 1 and 2. Clarifications for ensuring backwards compatibility with version 1 and 2 are given
in version 4 of this Command Class.

An implementation supporting Alarm CC V1 fields MUST map proprietary alarm types and levels
to a similar Notification Type and Notification CC V3 where possible. In addition, all Alarm CC V1
alarm types and levels MUST be described in the product manual.


**2.2.74.2.8** **Version** **4** **[DEPRECATED]**


Version 4 of this Command Class introduces the following:

 - Additional Notifications (refer to [36])


 Event/State = 0x00 (State idle) for a given Notification Type to indicate that all state variables
of that Notification Type returned to idle

 - The Zensor Net Source Node ID field has been discontinued. It is now a reserved field.

 - **Clarification** **to** **expected** **behavior** **in** **regards** **to:**


**–** V1 and V2 Alarm Get Command handling

**–** Notification Status field description

**–** Notification Type = 0xFF, “Return first detected notification on supported list”


**–** Event = 0xFE in Event Supported Report Command, which must not be advertised.


The support for state idle (event/state=0x00) cannot be advertised in the Event Supported Get
Command and version 4 nodes will appear to use reserved values for version 3 controlling nodes.



CC:0071.04.00.21.001 A version 4 node MUST comply with the rules outlined in Table 2.424 and Table 2.425.


Table 2.424 outlines the required behavior when receiving an Alarm Get command, Version 1.


Table 2.425 outlines the required behavior when receiving an Alarm Get command, Version 2.


The version of an Alarm Get Command can be determined from the command length.

|Table 2.424: Required behavior when receiving Alarm Get, version 1 Received Command: V1, ALARM_GET (Alarm Type = x)|Col2|
|---|---|
|**Received Command: V1, ALARM_GET (Alarm Type = x)**|**Received Command: V1, ALARM_GET (Alarm Type = x)**|
|V1 Alarm Type supported (x)?|Response|
|YES|V1, ALARM_REPORT (Alarm Type = x, Alarm Level = level)|
|NO|V1, ALARM_REPORT (Alarm Type = 0x00, Alarm Level =<br>0x00)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 350




<!-- PAGE 352 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024















|Table 2.425: Required behavior when receiving Alarm Get, version 2 Received Command: V2, ALARM_GET (Alarm Type = x, Z-Wave Alarm Type = y)|Col2|Col3|
|---|---|---|
|**Received Command: V2, ALARM_GET (Alarm Type = x, Z-Wave Alarm Type = y)**|**Received Command: V2, ALARM_GET (Alarm Type = x, Z-Wave Alarm Type = y)**|**Received Command: V2, ALARM_GET (Alarm Type = x, Z-Wave Alarm Type = y)**|
|Z-Wa<br>Alarm<br>Type<br>sup-<br>porte<br>(y)?|ve<br><br>d<br>V1<br>Alarm<br>Type<br>sup-<br>porte<br>(x)?|d<br>Response|
|NO|NO|NO RESPONSE|
|NO|YES|V2, ALARM_REPORT (<br>Alarm Type = x<br>Alarm Level = level<br>Reserved = 0x00<br>Z-Wave Alarm Status = 0x00<br>Z-Wave Alarm Type = 0x00<br>Z-Wave Alarm Event = 0x00<br>Number of Event Param = 0x00 )<br>|
|YES<br>or<br>y<br>=<br>0xFF|YES|/NO<br>Notifcations newer than V2, idle states or empty queues MUST be represented with<br>the unknown notifcation (Notifcation event/state feld set to 0xFE).<br>If no state is detected (push nodes) or no event/state queued (pull nodes), the<br>Notifcation Type MUST be set to one of the supported Notifcation Type in<br>response to a Get (Type = 0xFF)<br>**Push nodes:**<br>A supporting node MUST return the current states compatible with V2.<br>Table 2.427 shows a Push node example returning responses to diferent V2 Alarm<br>Get Commands.<br>**Pull nodes:**<br>A supporting node MUST return only V2 notifcations from its queue when receiving<br>a V2 Alarm Get Command.<br>A supporting node MUST set the status to 0x00 and event to 0xFE when its queue<br>is empty.<br>Table 2.428 shows a Pull node example returning responses to diferent V2 Alarm<br>Get Commands.|


Table 2.427 and Table 2.428 show the responses of a node supporting Notification Types and Notifications described in Table 2.426:

|Table 2.426: V2 Alarm Get node capabilities example Node capabilities|Col2|
|---|---|
|**Node capabilities**<br><br>|**Node capabilities**<br><br>|
|Notifcation Types|Notifcations|
|0x01: Smoke Alarm|0x01: Smoke detected<br>0x03: Smoke alarm test<br>0x06: Alarm silenced|
|0x03: CO2 Alarm|0x01: Carbon dioxide detected|



Table 2.427: Push node responses to V2 Alarm Get (example)
















|Received Get|Col2|Current states at the receiving<br>node|Col4|Col5|Returned response|Col7|Col8|
|---|---|---|---|---|---|---|---|
|V1 Alarm<br>Type|Type|Smoke<br>Alarm::<br>Sensor<br>status|Smoke<br>Alarm::<br>Alarm<br>status|CO2<br>Alarm::<br>Sensor<br>status|Type|Status|Event/<br>State|
|-*|0x01|Idle|Idle|-|0x01|0x00<br>or<br>0xFF|0xFE|



continues on next page


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 351




<!-- PAGE 353 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.427 – continued from previous page








































|Received Get|Col2|Current states at the receiving<br>node|Col4|Col5|Returned response|Col7|Col8|
|---|---|---|---|---|---|---|---|
|-|0x01|Smoke<br>detected<br>(V2)|Idle|-|0x01|0x00<br>or<br>0xFF|0x01|
|-|0x01|Smoke<br>detected<br>(V2)|Alarm<br>silenced<br>(V8)|-|0x01|0x00<br>or<br>0xFF|0x01|
|-|0x01|Idle|Smoke<br>alarm<br>test (V3)|-|0x01|0x00<br>or<br>0xFF|0xFE|
|0x00|0x02|-|-|-|No Report|No Report|No Report|
|0x01|0x02|-|-|-|No Report, unless V1 alarm is sup-<br>ported. Refer to _Required behavior_<br>_when receiving Alarm Get, version_<br>_2_|No Report, unless V1 alarm is sup-<br>ported. Refer to _Required behavior_<br>_when receiving Alarm Get, version_<br>_2_|No Report, unless V1 alarm is sup-<br>ported. Refer to _Required behavior_<br>_when receiving Alarm Get, version_<br>_2_|
|-|0xFF|Idle|Idle|Idle|0x01<br>or<br>0x03**|0x00<br>or<br>0xFF|0xFE|
|-|0xFF|Smoke<br>detected<br>(V2)|Idle|Idle|0x01|0x00<br>or<br>0xFF|0x01|
|-|0xFF|Smoke<br>detected<br>(V2)|Alarm<br>silenced<br>(V8)|Idle|0x01|0x00<br>or<br>0xFF|0x01|
|-|0xFF|Idle|Smoke<br>alarm<br>test (V3)|Idle|0x01|0x00<br>or<br>0xFF|0xFE|
|-|0xFF|Smoke<br>detected<br>(V2)|Idle|Carbon<br>dioxide<br>detected<br>(V2)|0x01<br>or<br>0x03**|0x00<br>or<br>0xFF|0x01|



*) The symbol ‘-’ indicates that the value has no impact on the V2 fields of the returned response

**) It is up to the node to decide which Notification Type to report.



Table 2.428: Pull node responses to V2 Alarm Get (example)















|Received Get|Col2|Before<br>returning a<br>report|Returned response|Col5|Col6|After re-<br>turning a<br>report|
|---|---|---|---|---|---|---|
|V1<br>Alarm<br>Type|Type|Node’s<br>queue|Type|Status|Event/<br>State|Node’s<br>queue|
|-*|0x01|Empty|0x01|0x00|0xFE|Empty|
|-|0x01|Carbon<br>dioxide<br>detected<br>(V2)<br>Smoke<br>de-<br>tected (V2)|0x01|0x00|0x01|Carbon<br>dioxide<br>detected<br>(V2)|
|-|0x01|Alarm<br>silenced<br>(V8)<br>Smoke<br>de-<br>tected (V2)|0x01|0x00|0x01|Alarm<br>silenced<br>(V8)|
|-|0x01|Alarm<br>silenced<br>(V8)|0x01|0x00|0xFE|Alarm<br>silenced<br>(V8)|


continues on next page



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 352




<!-- PAGE 354 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024






















|Received Get|Col2|Table 2.428 – Before|continued from previous page Returned response|Col5|Col6|After re-|
|---|---|---|---|---|---|---|
|**Received Get**|**Received Get**|**Before**<br>**returning a**<br>**report**|**Returned response**|**Returned response**|**Returned response**|**After**<br>**re-**<br>**turning**<br>**a**<br>**report**|
|0x00|0x02|•|No Report|No Report|No Report|-|
|0x01|0x02|•|No Report, unless V1 alarm is supported.<br>Refer to_ Required behavior when receiving_<br>_Alarm Get, version 2_|No Report, unless V1 alarm is supported.<br>Refer to_ Required behavior when receiving_<br>_Alarm Get, version 2_|No Report, unless V1 alarm is supported.<br>Refer to_ Required behavior when receiving_<br>_Alarm Get, version 2_|-|
|-|0xFF|Empty|0x01<br>or<br>0x03**|0x00|0xFE|Empty|
|-|0xFF|Carbon<br>dioxide<br>detected<br>(V2)<br>Smoke<br>de-<br>tected (V2)|0x03|0x00|0x01|Smoke<br>de-<br>tected (V2)|
|-|0xFF|Alarm<br>silenced<br>(V8)|0x01|0x00|0xFE|Alarm<br>silenced<br>(V8)|



*) The symbol ‘-’ indicates that the value has no impact on the V2 fields of the returned response

**) It is up to the node to decide which Notification Type to report.


**2.2.74.2.9** **Version** **5** **[DEPRECATED]**


Version 5 of this Command Class introduces additional Notifications (refer to [36]) and the event/state
parameters for the special purpose State idle 0x00, allowing to specify which state variable returned
to idle.


A version 4 controlling node will conclude that all state variables have returned to idle when a version
5 node advertises that a single state variable has returned to idle.


**2.2.74.2.10** **Version** **6** **[DEPRECATED]**


Version 6 of this Command Class introduces additional Notifications (refer to [36])

Version 6 clarifies how to use the ‘User Code Report’ Event Parameter. The User Code Report
Command is used as Event Parameter for the Notification {Access Control::Keypad Lock/Unlock
Operation} Command.

An example of Notification Event/State Parameter encapsulation is given in Section 2.2.74.6.1.


**2.2.74.2.11** **Version** **7** **[DEPRECATED]**


Version 7 of this Command Class introduces additional Notifications (refer to [36]).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 353




<!-- PAGE 355 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.74.2.12** **Version** **8**


CC:0071.08.00.22.001 It is RECOMMENDED that new nodes support version 8 of this Command Class.



CC:0071.08.00.23.001



Requirements for backwards compatibility with version 2 nodes introduced in version 4 have been
found to be ambiguous and challenging to be observed correctly by newer nodes. Therefore, it is
OPTIONAL for a version 8 node to comply with Table 2.425 when receiving a V2 Get Command.

Version 8 of this Command Class introduces additional Notifications (refer to [36]).



CC:0071.08.00.21.002
Version 8 increases the requirement level for the use of the “State idle” Notification from OPTIONAL
to REQUIRED.



CC:0071.08.00.21.003


CC:0071.08.00.21.004



Supporting nodes implementing version 8 or newer of the Notification Command Class MUST issue a
“State idle” Notification when a state variable returns to idle. For instance, the {Smoke alarm::Smoke
Detected} Notification MUST be followed by a {Smoke alarm::State idle(Smoke detected)} Notification when the smoke is no longer detected by the sensor. (refer to Figure 16).


**2.2.74.3** **Interoperability** **considerations**


**2.2.74.3.1** **Push** **nodes** **Basic** **control**



CC:0071.03.00.32.001 For Push nodes, it is RECOMMENDED to implement additional association groups for relevant
Notifications, which issue a Basic Set Command. It allows configuring a device to control other nodes
directly, e.g., turn on lights when motion is detected and turn off when there is no more motion.


**2.2.74.3.2** **Event** **flood**


CC:0071.03.00.32.002 Certain sensors may trigger repeatedly within a short amount of time. It is RECOMMENDED to
implement timers to arbitrate the transmission of notifications. Illustrations are given in Figure 23
and Figure 24.


Figure 2.22: Recommended timer mechanism for sending notifications (1)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 354




<!-- PAGE 356 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 2.23: Recommended timer mechanism for sending notifications (2)


**2.2.74.4** **Notification** **Set** **Command**


**Push** **nodes:**

This command is used to enable or disable the unsolicited transmission of a specific Notification Type.


**Pull** **nodes:**

This command is used to clear a persistent Notification in the notification queue.


Table 2.429: Notification Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|
|Command = NOTIFICATION_SET<br>|Command = NOTIFICATION_SET<br>|Command = NOTIFICATION_SET<br>|Command = NOTIFICATION_SET<br>|Command = NOTIFICATION_SET<br>|Command = NOTIFICATION_SET<br>|Command = NOTIFICATION_SET<br>|Command = NOTIFICATION_SET<br>|
|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|
|Notifcation Status|Notifcation Status|Notifcation Status|Notifcation Status|Notifcation Status|Notifcation Status|Notifcation Status|Notifcation Status|



**Notification** **Type** **(8** **bits)**

This field is used to specify a Notification Type. Assigned values are defined in [36].

CC:0071.03.06.11.001 A sending node MUST specify a Notification Type that is supported by a receiving node.

CC:0071.03.06.11.002 A receiving node MUST ignore the command if this field is set to a non-supported Notification Type
or if this field set to 0xFF.

**Notification** **Status** **(8** **bits)**


**Push** **nodes:**

This field is used to set the Status of a Notification Type.

This field MUST comply with Table 2.430.



CC:0071.03.06.11.004


CC:0071.03.06.11.005



Table 2.430: Notification Set::Notification Status (push mode)








|Value|Description|Version|
|---|---|---|
|0x00|Unsolicited messages MUST be disabled for the specifed Noti-<br>fcation Type<br>|2|
|0xFF|Unsolicited messages MUST be enabled for the specifed Noti-<br>fcation Type|2|



CC:0071.03.06.11.006 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0071.03.06.13.001


CC:0071.03.06.11.007


CC:0071.03.06.11.008

© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 355


CC0071030612001




<!-- PAGE 357 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A receiving node MAY deny the deactivation of a specific Notification Type. In that case, the receiving
node MUST respond to this command with an Application Rejected Request Command. Thus, if a
node can deny the deactivation of a Notification Type, the node MUST implement the Application
Status CC. A sending node should be aware that a receiving node may return a response to the Set
Command and thus SHOULD apply a back-off timer before sending a subsequent command.


**Pull** **nodes:**

CC:0071.05.11.009 A sending node MUST set this field to 0x00 to indicate that a persistent Notification for the specified
Notification Type MUST be cleared in the receiving node’s queue.


CC:0071.03.06.11.00A All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**2.2.74.5** **Notification** **Get** **Command**


**Push** **nodes:**

This command is used to request if the unsolicited transmission of a specific Notification
Type is enabled.


Some supporting nodes will also advertise a current state in response to this command.


**Pull** **nodes:**

This command is used to retrieve the next Notification from the receiving node’s queue.

CC:0071.03.04.11.001 The Notification Report Command MUST be returned in response to this command unless this
command is to be ignored. Refer to the fields description.


CC:0071.03.04.11.002 This command MUST NOT be issued via multicast addressing.


CC:0071.03.04.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.431: Notification Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|
|Command = NOTIFICATION_GET|Command = NOTIFICATION_GET|Command = NOTIFICATION_GET|Command = NOTIFICATION_GET|Command = NOTIFICATION_GET|Command = NOTIFICATION_GET|Command = NOTIFICATION_GET|Command = NOTIFICATION_GET|
|V1 Alarm Type<br>|V1 Alarm Type<br>|V1 Alarm Type<br>|V1 Alarm Type<br>|V1 Alarm Type<br>|V1 Alarm Type<br>|V1 Alarm Type<br>|V1 Alarm Type<br>|
|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|
|Notifcation Event / State|Notifcation Event / State|Notifcation Event / State|Notifcation Event / State|Notifcation Event / State|Notifcation Event / State|Notifcation Event / State|Notifcation Event / State|



**V1** **Alarm** **Type** **(8** **bits)**

The use of this field depends on the V1 Alarm field advertised in the Alarm Type Supported Report
Command.


A sending node MAY specify a V1 Alarm Type if the receiving node supports the actual alarm type.


A sending node MUST specify the value 0x00 if the receiving node does not support V1 alarms.


CC:0071.03.04.12.001 The receiving node behavior SHOULD comply with Table 2.424 and Table 2.425.

**Notification** **Type** **(8** **bits)**

This field is used to specify a Notification Type. Assigned values are defined in [36].

CC:0071.03.04.11.004 This field MUST be set to a Notification Type that is supported by the receiving node or to 0xFF.

CC:0071.03.04.11.005 A receiving node MUST ignore the command if this field is different than 0xFF and set to a
non-supported Notification Type.


**Push** **nodes:**


CC:0071.03.04.12.002


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 356




<!-- PAGE 358 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value 0xFF indicates to the receiving node that it MUST select a supported Notification Type
and SHOULD advertise the current state of one of its state variables within the chosen Notification
Type.


CC:0071.03.04.11.006
A supported Notification Type value indicates that the receiving node MUST advertise the unsolicited
transmission status for the requested Notification Type and MAY advertise the current state of one
of its state variables within the Notification Type.


**Pull** **nodes:**

CC:0071.03.04.11.007 The value 0xFF indicates to the receiving node that it MUST retrieve the next Notification in its

queue.

CC:0071.03.04.12.003 A Notification Type value indicates to the receiving node that it SHOULD retrieve the next Notification in its Notification queue matching the specified Notification Type value.

**Notification** **Event** **/** **State** **(8** **bits)**

This field is used to optionally specify a Notification Event/State within the Notification Type. Assigned values are defined in [36]. This field allows receiving nodes to differentiate between V2 Alarm
Get Command and V3 or newer Notification Get Command.


CC:0071.03.04.11.008
If the Notification Type is set to 0xFF, this field MUST be set to 0x00 by a sending node and SHOULD
be ignored by a receiving node.


**Push** **nodes:**

CC:0071.03.04.13.001 A sending node MAY set this field to 0x00.

CC:0071.03.04.13.002 A sending node MAY specify a value that is supported by the receiving node within the specified
Notification Type. In this case, a receiving node:


         - MAY advertise a current state related to the indicated state - MAY return the same value in response
to a supported Notification Event.

CC:0071.03.04.11.009 A receiving node MUST return the “Unknown notification” value (0xFE) in response to a nonsupported Notification Event.


**Pull** **nodes:**

CC:0071.03.04.12.004 This field SHOULD be ignored by a receiving node.


**2.2.74.6** **Notification** **Report** **Command**


**Push** **nodes:**


This command is used for two purposes:

       - If this command is returned in response to a Notification Get Command, this command advertises if the unsolicited transmission of the advertised Notification Type is
enabled and optionally advertises a currently active state.

       - If this command is sent unsolicited, it advertises an event or state Notification.

The use of the command’s fields is the same in both cases.


**Pull** **nodes:**

This command is used by a sending node to return a Notification from its queue or indicate
that its queue is empty.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 357




<!-- PAGE 359 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.432: Notification Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|
|Command = NOTIFICATION_REPORT|Command = NOTIFICATION_REPORT|Command = NOTIFICATION_REPORT|Command = NOTIFICATION_REPORT|Command = NOTIFICATION_REPORT|Command = NOTIFICATION_REPORT|Command = NOTIFICATION_REPORT|Command = NOTIFICATION_REPORT|
|V1 Alarm Type|V1 Alarm Type|V1 Alarm Type|V1 Alarm Type|V1 Alarm Type|V1 Alarm Type|V1 Alarm Type|V1 Alarm Type|
|V1 Alarm Level|V1 Alarm Level|V1 Alarm Level|V1 Alarm Level|V1 Alarm Level|V1 Alarm Level|V1 Alarm Level|V1 Alarm Level|
|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|
|Notifcation Status<br>|Notifcation Status<br>|Notifcation Status<br>|Notifcation Status<br>|Notifcation Status<br>|Notifcation Status<br>|Notifcation Status<br>|Notifcation Status<br>|
|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|Notifcation Type<br>|
|Notifcation Event / State|Notifcation Event / State|Notifcation Event / State|Notifcation Event / State|Notifcation Event / State|Notifcation Event / State|Notifcation Event / State|Notifcation Event / State|
|Sequence|Reserved|Reserved|Event / State Parameters Length|Event / State Parameters Length|Event / State Parameters Length|Event / State Parameters Length|Event / State Parameters Length|
|Event /State Parameter 1 (optional)|Event /State Parameter 1 (optional)|Event /State Parameter 1 (optional)|Event /State Parameter 1 (optional)|Event /State Parameter 1 (optional)|Event /State Parameter 1 (optional)|Event /State Parameter 1 (optional)|Event /State Parameter 1 (optional)|
|…|…|…|…|…|…|…|…|
|Event / State Parameter N (optional)|Event / State Parameter N (optional)|Event / State Parameter N (optional)|Event / State Parameter N (optional)|Event / State Parameter N (optional)|Event / State Parameter N (optional)|Event / State Parameter N (optional)|Event / State Parameter N (optional)|
|Sequence Number (optional)|Sequence Number (optional)|Sequence Number (optional)|Sequence Number (optional)|Sequence Number (optional)|Sequence Number (optional)|Sequence Number (optional)|Sequence Number (optional)|



**Reserved**

CC:0071.03.05.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**V1** **Alarm** **Type** **(8** **bits)** **&** **V1** **Alarm** **Level** **(8** **bits)**

These fields carry the proprietary Alarm Type and Alarm Level fields originally introduced with Alarm
CC:0071.03.05.11.002 Command Class, Version 1. V1 Alarm Type and V1 Alarm Level fields MUST be specified in the
product manual.

CC:0071.03.05.11.003 If the V1 Alarm Type is not supported, these fields MUST be set to 0x00.

**Notification** **Status** **(8** **bits)**


**Push** **nodes:**

This field is used to advertise the status of the Notification Type indicated in this command.

CC:0071.03.05.11.004 This field MUST comply with Table 2.433.



Table 2.433: Notification Report::Notification Status (push nodes)








|Value|Description|Version|
|---|---|---|
|0x00|Unsolicited transmissions are disabled for the specifed Notif-<br>cation Type<br>|2|
|0xFF|Unsolicited transmissions are enabled for the specifed Notifca-<br>tion Type|2|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Pull** **nodes:**

This field is used to advertise the status of the sending node’s Notification queue.

CC:0071.03.05.11.005 This field MUST comply with Table 2.434.



Table 2.434: Notification Report::Notification Status (pull nodes)








|Value|Description|Version|
|---|---|---|
|0x00|This command carries a valid Notifcation returned from the<br>queue.<br>There may be more Notifcations queued up. This Notifcation<br>MAY be persistent.<br>|2|
|0xFE|This command does not carry any valid Notifcation and the<br>event queue is empty|3|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 358




<!-- PAGE 360 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**Notification** **Type** **(8** **bits)**

This field is used to advertise the Notification Type. Assigned values are defined in [36].

CC:0071.03.05.11.006 A sending node MUST set this field to the Notification Type of the actual Notification.

**Notification** **Event** **/** **State** **(8** **bits)**

This field is used to specify a Notification Event/State for the advertised Notification Type. Assigned
values are defined in [36].

CC:0071.03.05.11.007 A node advertising a Notification MUST set this field to the actual Notification event/state.


**Sequence** **(1** **bit)**

This field is used to advertise the presence of the “Sequence Number” field.

CC:0071.03.05.11.008 The value 0 MUST indicate that no “Sequence Number” field is appended after the “Event / State
Parameter” field.

CC:0071.03.05.11.009 The value 1 MUST indicate that a “Sequence Number” field is appended after the “Event / State
Parameter” field.


**Event** **/** **State** **Parameters** **Length** **(5** **bits)**

This field is used to advertise the length in bytes of the Event / State Parameters field.

CC:0071.03.05.11.00A The value 0 MUST indicate that no Event / State Parameter field is appended after the Event
Parameters Length field.

CC:0071.03.05.11.00B Values in the range 1..31 MUST indicate the length of the Event / State Parameter field appended
after the Event / State Parameters Length field.


**Event** **/** **State** **Parameter** **(N** **bytes)**

The Event / State Parameter field is used to specify associated parameters to a Notification.

Parameters for each Event/State Notification are defined in [36].

CC:0071.03.05.11.00CCC:0071.03.05.13.001 This field MAY carry an encapsulated command. In this case, the field MUST include the complete
command structure, i.e. Command Class, Command and all mandatory command fields.


CC:0071.03.05.11.00D
If a node encapsulates a command in this field, the corresponding Command Class MUST be supported
by the node and advertised in the Node Information Frame (NIF) or S0/S2 Supported Command
Report.

CC:0071.03.05.11.00E This field MUST be omitted if the “Event Parameter Length” field is set to 0.


Section 2.2.74.6.1 provides an example of Event Parameter encapsulation.


**Sequence** **Number** **(8** **bits)**

CC:0071.03.05.13.002 This field is used to advertise a sequence number for the actual Notification. This command MAY
carry a Sequence Number field.

CC:0071.03.05.11.00F This field MUST be omitted if the Sequence flag is set to 0.

CC:0071.03.05.11.010 The first sequence number for each distinct Notification MUST be 1. A sending node MUST increment the sequence number for a Notification each time it issues a Notification Report for that given
Notification.


CC:0071.03.05.11.011 The Sequence Number range MUST be in the range 0..255. The value after 255 MUST be 0.


Example:

1. Notification {Smoke Alarm::Smoke Detected}, …, Seq. Number = 254

2. Notification {Smoke Alarm::Smoke Detected}, …, Seq. Number = 255

3. Notification {Heat Alarm::Overheat Detected}, …, Seq. Number = 6

4. Notification {Smoke Alarm::Smoke Detected}, …, Seq. Number = 0


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 359




<!-- PAGE 361 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


5. Etc.


**2.2.74.6.1** **Event** **/** **State** **parameter** **encapsulation**


CC:0071.03.05.11.012 Event / State parameter encapsulation of commands MUST comprise the entire command, starting
from the Command Class identifier.


For example, a “User Code Report” is used as Event / State Parameter in a “Keypad Lock/Unlock
Operation”. The “User Code Report” has the following format:


      - Command Class =COMMAND_CLASS_USER_CODE = 0x63


      - Command = USER_CODE_REPORT = 0x03

      - User Identifier = 0x01


      - User ID Status = 0x01


      - User Code = 0x30, 0x30, 0x30, 0x30


The complete User Code Report therefore comprises the following Bytes: [0x63, 0x03, 0x01, 0x01,
0x30, 0x30, 0x30, 0x30].


Another example with the Node naming and location Command class is given in Table 2.435.


Table 2.435: Notification Report::Event / State parameter encap
|Table 2.435: Notification Report: sulation (example) Notification Report Command fields|Col2|::Event / S Value|State parameter encap- Explanation|
|---|---|---|---|
|**Notifcation Report Command felds**|**Notifcation Report Command felds**|**Value**|**Explanation**<br>|
|1|COMMAND_CLASS_NOTIFICA-<br>TION|0x71|Notifcation CC id<br>|
|2|NOTIFICATION_REPORT|0x05|Notifcation Report command id|
|3|V1 Alarm Type|0x00|Not implemented|
|4|V1 Alarm Level|0x00|Not implemented<br>|
|5|Reserved<br>|0x00|Reserved feld|
|6|Notifcation Status<br>|0xFF|Unsolicited report is activated|
|7|Notifcation Type<br>|0x01|Smoke Alarm|
|8|Notifcation Event|0x01|Smoke Detected|
|9|Sequence Number / Event Parameters<br>Length|0x1A|Sequence<br>Number<br>is<br>appended<br>/<br>Event Parm Length = 10|
|10|Event Parm 1|0x77|Node Naming & Location CC id|
|11|Event Parm 2|0x06|Node Location Report command id|
|12|Event Parm 3|0x00|Cmd Parm: Char = ASCII|
|13|Event Parm 4|0x4B|Cmd Parm: Node Location Char 1 =<br>K|
|14|Event Parm 5|0x49|Cmd Parm: Node Location Char 2 =<br>I|
|15|Event Parm 6|0x54|Cmd Parm: Node Location Char 3 =<br>T|
|16|Event Parm 7|0x43|Cmd Parm: Node Location Char 4 =<br>C|
|17|Event Parm 8|0x48|Cmd Parm: Node Location Char 5 =<br>H|
|18|Event Parm 9|0x45|Cmd Parm: Node Location Char 6 =<br>E|
|19|Event Parm 10|0x4E|Cmd Parm: Node Location Char 7 =<br>N|
|20|Sequence Number|0x0F|Sequence Number = 15|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 360




<!-- PAGE 362 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.74.7** **Notification** **Supported** **Get** **Command**


This command is used to request supported Notification Types.

CC:0071.03.07.11.001 The Notification Supported Report Command MUST be returned in response to this command.


CC:0071.03.07.11.002 This command MUST NOT be issued via multicast addressing.


CC:0071.03.07.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.436: Notification Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|
|Command = NOTIFICATION_SUPPORTED_GET|Command = NOTIFICATION_SUPPORTED_GET|Command = NOTIFICATION_SUPPORTED_GET|Command = NOTIFICATION_SUPPORTED_GET|Command = NOTIFICATION_SUPPORTED_GET|Command = NOTIFICATION_SUPPORTED_GET|Command = NOTIFICATION_SUPPORTED_GET|Command = NOTIFICATION_SUPPORTED_GET|



**2.2.74.8** **Notification** **Supported** **Report** **Command**


This command is used to advertise supported Notification Types.


Table 2.437: Notification Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|
|Command = NOTIFICATION_SUPPORTED_REPORT|Command = NOTIFICATION_SUPPORTED_REPORT|Command = NOTIFICATION_SUPPORTED_REPORT|Command = NOTIFICATION_SUPPORTED_REPORT|Command = NOTIFICATION_SUPPORTED_REPORT|Command = NOTIFICATION_SUPPORTED_REPORT|Command = NOTIFICATION_SUPPORTED_REPORT|Command = NOTIFICATION_SUPPORTED_REPORT|
|V1 Alarm|Reserved|Reserved|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**V1** **Alarm** **(1** **bit)**

This field is used to indicate if the node implements proprietary Alarms from version 1.


CC:0071.03.08.11.001
The value 0 MUST indicate that the device implements only Notification CC V2 or newer Notification
Types.


CC:0071.03.08.11.002
The value 1 MUST indicate that the device implements Notification CC V2 Notification Types as well
as proprietary Alarm CC V1 Alarm Types and Alarm Levels.


**Number** **of** **Bit** **Masks** **(5** **bits)**

CC:0071.03.08.11.003 This field MUST advertise the length in bytes of the Bit Mask field.


The value MUST be in the range 1..31.


**Bit** **Mask** **(N** **bytes)**

The Bit Mask field describes the supported Notification Types by the node. The length of this field
CC:0071.03.08.11.004 in bytes MUST match the value advertised in the Number of Bit Masks field.

      - Bit 0 in Bit Mask 1 is not allocated to any Notification Type and MUST be set to zero.

      - Bit 1 in Bit Mask 1 indicates if Notification Type = Smoke Alarm (0x01) is supported.

      - Bit 2 in Bit Mask 1 indicates if Notification Type = CO Alarm (0x02) is supported.

      - Bit 3 in Bit Mask 1 indicates if Notification Type = CO2 Alarm (0x03) is supported


      - …

For Notification Types, refer to [36].

CC:0071.03.08.11.005 If the Notification Type is supported, the corresponding bit MUST be set to 1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 361




<!-- PAGE 363 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If the Notification Type is not supported, the corresponding bit MUST be set to 0.

CC:0071.03.08.11.006 The Notification Type values 0x00 and 0xFF are special-purpose values. Reserved values and
special-purpose values MUST NOT be advertised in the Bit Mask field by a sending node and MUST
be ignored by a receiving node.


**2.2.74.9** **Event** **Supported** **Get** **Command**


This command is used to request the supported Notifications for a specified Notification Type.


CC:0071.03.01.11.001 The Event Supported Report Command MUST be returned in response to this command.


CC:0071.03.01.11.002 This command MUST NOT be issued via multicast addressing.


CC:0071.03.01.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.438: Event Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|
|Command = EVENT_SUPPORTED_GET<br>|Command = EVENT_SUPPORTED_GET<br>|Command = EVENT_SUPPORTED_GET<br>|Command = EVENT_SUPPORTED_GET<br>|Command = EVENT_SUPPORTED_GET<br>|Command = EVENT_SUPPORTED_GET<br>|Command = EVENT_SUPPORTED_GET<br>|Command = EVENT_SUPPORTED_GET<br>|
|Notifcation Type|Notifcation Type|Notifcation Type|Notifcation Type|Notifcation Type|Notifcation Type|Notifcation Type|Notifcation Type|



**Notification** **Type** **(8** **bits)**

For Notifications Types, refer to [36].

If a node receives an unsupported Notification Type or a special-purpose value, the receiving node
CC:0071.03.01.11.004 MUST respond with Event Supported Report Command with the Notification Type specified in the
this command and the Number of Bit Masks field set to 0.


**2.2.74.10** **Event** **Supported** **Report** **Command**


This command is used to advertise supported events/states for a specified Notification Type.


Table 2.439: Event Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|Command Class = COMMAND_CLASS_NOTIFICATION|
|Command = EVENT_SUPPORTED_REPORT<br>|Command = EVENT_SUPPORTED_REPORT<br>|Command = EVENT_SUPPORTED_REPORT<br>|Command = EVENT_SUPPORTED_REPORT<br>|Command = EVENT_SUPPORTED_REPORT<br>|Command = EVENT_SUPPORTED_REPORT<br>|Command = EVENT_SUPPORTED_REPORT<br>|Command = EVENT_SUPPORTED_REPORT<br>|
|Notifcation Type|Notifcation Type|Notifcation Type|Notifcation Type|Notifcation Type|Notifcation Type|Notifcation Type|Notifcation Type|
|Reserved|Reserved|Reserved|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Notification** **Type** **(8** **bits)**

For Notifications Types, refer to [36].


**Number** **of** **Bit** **Masks** **(5** **bits)**

This field is used to advertise the length (in bytes) of the Bit Mask field.


CC:0071.03.02.11.001 The value MUST be in the range 0..31.

The value 0 MUST indicate that the Notification Type is not supported.


**Bit** **Mask** **(N** **bytes)**


CC:0071.03.02.11.002


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 362




<!-- PAGE 364 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to advertise the supported Events/States for the actual advertised Notification Type.
The length of this field (in bytes) MUST match the value advertised in the Number of Bit Masks field.
This field MUST be omitted if the “Number of Bit Masks” field is set to 0.


CC:0071.03.02.11.003 The bit value ‘1’ MUST indicate that the actual Event/State is supported.


The bit value ‘0’ MUST indicate that the actual Event/State is not supported.

Example: Notification Type = Heat Alarm (0x04):

      - Bit 0 in Bit Mask 1 field is not allocated to any event and must therefore be set to zero.

      - Bit 1 in Bit Mask 1 field indicates support for Overheat detected (0x01).

      - Bit 2 in Bit Mask 1 field indicates support for Overheat, unknown loc. (0x02).

      - Bit 3 in Bit Mask 1 field indicates support for Rapid temp rise (0x03).


      - …

For Notification Types and their Events/States, refer to [36].


The Event/State values 0x00 and 0xFE are special-purpose values. Reserved values and
CC:0071.03.02.11.004 special-purpose values MUST NOT be advertised in the Bit Mask field by a sending node and MUST
be ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 363