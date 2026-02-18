<!-- PAGE 606 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.8** **Association** **Group** **Information** **(AGI)** **Command** **Class,** **version** **1**


The Association Group Information (AGI) Command Class allows a node to advertise the capabilities
of each association group supported by a given application resource.


CC:0059.01.00.12.001 Controllers and installer tools SHOULD use AGI information to support controller-assisted
button-to-button association and GUI-based drag-and-drop association in a plug-and-play fashion.


Centralized gateway-based deployments may create a single association from the lifeline association
group to a central management application.


**3.2.8.1** **Compatibility** **considerations**


CC:0059.01.00.21.001 A node supporting the AGI Command Class MUST support the Association Command Class.


**3.2.8.1.1** **Multi** **Channel** **considerations**


The Association Group Information (AGI) Command Class also applies to Multi Channel devices.


If a node implements Multi Channel End Points and supports the AGI Command Class, each indiCC:0059.01.00.21.002 vidual End Point MUST support the AGI Command Class.


**3.2.8.2** **Association** **Principles**


A light control transmitter may have one or more keys. A key is mapped to one or more association

groups.


Figure 3.1: Light Control Transmitter (example)


Figure 3.2: Lamp Module (example)


A light control transmitter key can be configured to control a lamp by adding the NodeID of the lamp
to an association group that represents the key.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 605




<!-- PAGE 607 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.8.3** **The** **Association** **Group** **Information**


A node may implement one or more association groups. If the device implements association groups,
CC:0059.01.00.12.002 the device SHOULD provide an Association Group Information (AGI) table as described in Table
3.25.



Table 3.25: Layout of One Line of the Association Group Information Table








|Group<br>i<br>identifer|i<br>Profle 2<br>bytes|Command Class & Command (list)<br>N bytes|Group Name (UTF -8) M<br>bytes|
|---|---|---|---|
|||||



CC:0059.01.00.11.001


CC:0059.01.00.11.002


CC:0059.01.00.13.001



An AGI table entry carries a number of fields. The information is typically static and can be defined
at compile time. Thus, the AGI table does not need to occupy any RAM or non-volatile storage.


**3.2.8.3.1** **Group** **identifier**


The Group identifier indicates which association group the actual table entry relates to. As association
groups are always numbered in a sequence starting from 1, an actual implementation does not have
to store the group identifier in its memory. The number of association groups may be requested via
the Association Groupings Get or Multi Channel Association Groupings Get commands.


Association group 1 is reserved for the Z-Wave Plus Lifeline association group. Group 1 MUST NOT
be assigned to any other use than the Lifeline group. The actual Device Type specifies a mandatory
list of commands which the device MUST send to all targets associated to the Lifeline group. A
manufacturer MAY add additional commands to the Lifeline group. Refer to [34] and _Device_ _Type_ _v2_
_Specification_ .



CC:0059.01.00.11.003 The Lifeline group MUST be advertised for the Root Device of a Multi Channel device. A Multi

CC:0059.01.00.12.003 Channel End Point SHOULD advertise commands for association group 1 which End Points can send
via the Root Device Lifeline group if a Multi Channel Association is created from the Root Device
Lifeline group.


**3.2.8.3.2** **Profile**


CC:0059.01.00.13.002 A device MAY implement one or several AGI profiles. The profile defines the scope of events which
triggers the transmission of commands to the actual association group. As an example a temperature
sensor may issue different Basic Set Command parameters when the temperature exceeds a threshold
and when the temperature drops below a threshold. The actual behavior is application dependent
and out of scope of the AGI Command Class.

The profile identifiers are referenced in Table 3.36       - _AGI_ _Profiles_ . Profiles are divided into categories
in the following sections.


**3.2.8.3.3** **General** **profiles**


The “General” category comprises the “Not Applicable” and “Lifeline” profiles. The “Not Applicable”

CC:0059.01.00.11.004
profile identifier MUST be advertised if the actual association group does not match any of the defined
profiles.

CC:0059.01.00.11.005 The “Lifeline” profile identifier MUST be advertised for association group 1 of the Root Device.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 606




<!-- PAGE 608 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.8.3.4** **Control** **profiles**


“Control” profiles are intended for association groups of which commands are triggered by a user
control mechanism, such as keys or buttons. As an example, a light control transmitter may comprise
two control keys that can each control a group of lamps.

A control key may control up and down dimming as well as on/off state. Thus, a control key may
send more than one command with one specific parameter. A control key may be implemented as a
physical key, a group of icons, touch screen gestures or other means. The actual implementation is
out of scope of this command class.


CC:0059.01.00.13.003 In case of multiple logical functions in a device, the device MAY implement one Multi Channel End
Point for each logical function; e.g. each push button is implemented as a separate End Point. Table
3.26 gives an example of a Multi Channel a battery-powered two-button light control device.










































|Table 3.26: Example: AGI Tables for Two-Button Light Control Transmitter Root Device:|Col2|Col3|Col4|
|---|---|---|---|
|Root Device:<br>|Root Device:<br>|Root Device:<br>|Root Device:<br>|
|**Group**<br>**identi-**<br>**fer**|**Profle**<br>**2 bytes**|**Command Class & Command (list) N bytes**<br>|**Group Name**<br>**(UTF-8) M**<br>**bytes**|
|1|General:<br>Lifeline|Central Scene Notifcation<br>Notifcation Report<br>Battery Report<br>Device Reset Locally Notifcation|Lifeline<br>|
|2|Control:<br>Key1|Basic Set|On/Of control<br>(Button 1)|
|3|Control:<br>Key1|Multilevel Switch Set|Dimmer control<br>(Button 1)<br>|
|4|Control:<br>Key2|Basic Set|On/Of control<br>(Button 2)|
|5|Control:<br>Key2|Multilevel Switch Set|Dimmer control<br>(Button 2)|
|End Point 1:<br>|End Point 1:<br>|End Point 1:<br>|End Point 1:<br>|
|**Group**<br>**identi-**<br>**fer**|**Profle**<br>**2 bytes**|**Command Class & Command (list) N bytes**|**Group Name**<br>**(UTF-8) M**<br>**bytes**|
|1|General:<br>Lifeline|-|Lifeline<br>|
|2|Control:<br>Key1|Basic Set|On/Of control<br>(Button 1)|
|3|Control:<br>Key1|Multilevel Switch Set|Dimmer control<br>(Button 1)|
|End Point 2:<br>|End Point 2:<br>|End Point 2:<br>|End Point 2:<br>|
|**Group**<br>**identi-**<br>**fer**|**Profle**<br>**2 bytes**|**Command Class & Command (list) N bytes**|**Group Name**<br>**(UTF-8) M**<br>**bytes**|
|1|General:<br>Lifeline|-|Lifeline<br>|
|2|Control:<br>Key2|Basic Set|On/Of control<br>(Button 1)|
|3|Control:<br>Key2|Multilevel Switch Set|Dimmer control<br>(Button 1)|



The Profile identifiers Control:Key 1 and Control:Key 2 allows an installer tool to determine which
Multi Channel End Point and which association group to use in order to configure buttons to control a
light dimmer. The Group Name allows a human user to make a qualified decision even if the installer
tool is not, e.g. because it is running an older version not updated with newer profile identifiers.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 607




<!-- PAGE 609 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


End Points 1 and 2 in the above example do not support any Command Class that must be sent via
the Z-Wave Plus Lifeline. Therefore End Points 1 and 2 advertise an empty Command Class list for
the Lifeline association group.


The Root Device in the above example advertises the Basic Set Command in association group 2.
CC:0059.01.00.12.004 This is a feature of End Point 1. A controlling node SHOULD NOT create associations from other
Root Device association groups than the Lifeline group if it supports the Multi Channel Command
Class. The purpose of the Root Device Association Groups (with the exception of the Lifeline group)
is only to provide backwards compatibility for legacy devices without support for the Multi Channel
Command Class.


**3.2.8.3.5** **Sensor** **profiles**


“Sensor” profiles are intended for association groups of which commands are triggered by sensor
readings. As an example, a sensor product could comprise two temperature sensors.

Sensor profile identifiers are constructed by prepending the Multilevel Sensor Command Class identifier
(referred to with AGI_PROFILE_SENSOR) to a multilevel sensor type defined in the Multilevel
Sensor Command Class. The values in Table 8 only serve as examples to illustrate the construction
of AGI Sensor Profile Identifiers. For the full list of available sensor types, refer to the “Multilevel
Sensor Report Command”.


CC:0059.01.00.12.005 In case of multiple logical functions in a device, the device SHOULD implement one Multi Channel
End Point for each logical function; e.g. each sensor instance is implemented as a separate End Point.
Table 3.27 gives an example of a Multi Channel battery-powered sensor device with two multilevel
sensor functions:


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 608




<!-- PAGE 610 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024
















































|Table 3.27: Example: AGI Tables for Two-Function Sensor Root Device:|Col2|Col3|Col4|
|---|---|---|---|
|Root Device:<br>|Root Device:<br>|Root Device:<br>|Root Device:<br>|
|**Group**<br>**identi-**<br>**fer**|**Profle 2**<br>**bytes**|**Command Class & Command (list) N**<br>**bytes**<br>|**Group Name**<br>**(UTF-8) M bytes**|
|1|General:<br>Lifeline|Multilevel Sensor Report Notifcation Report<br>Battery Report Device Reset Locally<br>Notifcation|Lifeline<br>|
|2|Sensor:<br>Tempera-<br>ture|Basic Set|On/Of control<br>(Indoor<br>temperature)<br>|
|3|Sensor:<br>Tempera-<br>ture|Basic Set|On/Of control<br>(Outdoor<br>temperature)|
|End Point 1<br>|End Point 1<br>|End Point 1<br>|End Point 1<br>|
|**Group**<br>**identi-**<br>**fer**|**Profle 2**<br>**bytes**|**Command Class & Command (list) N**<br>**bytes**|**Group Name**<br>**(UTF-8) M bytes**|
|1|Sensor:<br>Tempera-<br>ture|Multilevel Sensor Report|Indoor temperature<br>via Lifeline<br>|
|2|Sensor:<br>Tempera-<br>ture|Basic Set|On/Of control<br>(Indoor<br>temperature)|
|End Point 2<br>|End Point 2<br>|End Point 2<br>|End Point 2<br>|
|**Group**<br>**identi-**<br>**fer**|**Profle 2**<br>**bytes**|**Command Class & Command (list) N**<br>**bytes**|**Group Name**<br>**(UTF-8) M bytes**|
|1|Sensor:<br>Tempera-<br>ture|Multilevel Sensor Report|Outdoor<br>temperature via<br>Lifeline<br>|
|2|Sensor:<br>Tempera-<br>ture|Basic Set|On/Of control<br>(Outdoor<br>temperature)|



The Profile identifier is Sensor:Temperature for both End Points but the Group Name allows a user
to determine which End Point and which association group to use in order to configure the indoor
temperature sensor to control a heating element.


The Root Device in the above example advertises the Multilevel Sensor Report command in the
Lifeline group. Residing in a Multi Channel device, the Root Device does not actually implement
any application functionality. The Multilevel Sensor Report Command is a feature of the End Points
which is advertised for backwards compatibility with legacy devices not supporting the Multi Channel
Command Class.


Likewise, the Root device advertises the Basic Set Command in association groups 2 and 3. This is
also a feature of the End Points. Refer to the Multi Channel Command Class for details on backwards

compatibility.


End Point 1 in the above example advertises the Multilevel Sensor Report Command in association
group 1. By advertising that zero NodeIDs are supported for association group 1, End Point 1 indicates
that this command is sent via the Root Device Lifeline group if a Multi Channel association is created
for the Root Device Lifeline group. The same principle applies to End Point 2.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 609




<!-- PAGE 611 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.8.3.6** **Notification** **profiles**


“Notification” profiles are intended for association groups of which commands are triggered by detected
events or state changes. As an example, a detector product could comprise one smoke sensor and one
CO2 detector.

Notification profile identifiers are constructed by prepending the Notification Command Class identifier
(referred to with AGI_PROFILE_NOTIFICATION) to a notification type defined in the Notification
Command Class. The values below only serve as an example to illustrate the construction of AGI
Notification Profile identifiers. For the full list of available notification types, refer to the Notification
Command Class (Section 2).


CC:0059.01.00.12.006 In case of multiple logical functions in a device, the device SHOULD implement one Multi Channel
End Point for each logical function.


The following example outlines how a standalone smoke alarm is represented by an AGI table:
















|Table 3.28: Example: AGI Table for One-Function Alarm Device Root Device:|Col2|Col3|Col4|
|---|---|---|---|
|Root Device:<br>|Root Device:<br>|Root Device:<br>|Root Device:<br>|
|**Group**<br>**identifer**|**Profle 2**<br>**bytes**|**Command Class & Command (list) N**<br>**bytes**<br>|**Group Name**<br>**(UTF-8) M bytes**|
|1|General:<br>Lifeline<br>|Notifcation Report Battery Report Device<br>Reset Locally Notifcation|Lifeline<br>|
|2|Notifca-<br>tion|Basic Set|On/Of control<br>(Smoke)|



The Profile identifier Notification SmokeAlarm indicates to an installer that the Basic Set Command
of association group 2 is issued in response to smoke alarm events.


**3.2.8.3.7** **Command** **Class** **and** **Command**


This field contains the command class and the command that is sent to targets associated with this
CC:0059.01.00.13.004 association group if an event occurs. This field MAY advertise a list of commands and MAY contain
a combination of extended and normal command classes. Refer to Section 3.2.8.9.


The command list is used by a controlling application to discover what functionality the node provides
via a given association group. It also allows the controlling node to ensure that the associated node
understands the received commands.

CC:0059.01.00.13.005 A node MAY list only one command if the actual association group sends different commands which
actually relate to the same overall functionality and belong to the same Command Class and Commands Class version (e.g. Multilevel Switch Set / Multilevel Switch Start Level Change / Multilevel
Stop Level Change)


In case Multi Channel End Points are implemented, the Lifeline association group (group 1) of End
CC:0059.01.00.12.007 Points SHOULD be used to advertise commands that will be sent via the Root Device Lifeline group
if a Multi Channel association is created from the Root Device Lifeline group.


**3.2.8.3.8** **Association** **group** **name**


This field contains a name reflecting the purpose of the group, e.g. “On/Off control (Smoke)”.


CC:0059.01.00.11.006 The Root Device Lifeline group MUST be named “Lifeline”.


CC:0059.01.00.11.007 Group names MUST be encoded using UTF-8. The available capacity for characters depends on the
actual characters encoded with UTF-8. Plain ASCII characters only occupy one byte while special
characters may need two or more bytes for representation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 610




<!-- PAGE 612 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.8.4** **Association** **Group** **Name** **Get**


This command is used to query the name of an association group.


CC:0059.01.01.11.001 The Association Group Name Report Command MUST be returned in response to this command.


CC:0059.01.01.11.002 This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.29: Association Group Name Get

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|
|Command = ASSOCIATION_GROUP_NAME_GET<br>|Command = ASSOCIATION_GROUP_NAME_GET<br>|Command = ASSOCIATION_GROUP_NAME_GET<br>|Command = ASSOCIATION_GROUP_NAME_GET<br>|Command = ASSOCIATION_GROUP_NAME_GET<br>|Command = ASSOCIATION_GROUP_NAME_GET<br>|Command = ASSOCIATION_GROUP_NAME_GET<br>|Command = ASSOCIATION_GROUP_NAME_GET<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|



**Grouping** **Identifier** **(1** **byte)**

This field is used to specify the requested association group identifier.

CC:0059.01.01.12.001 A node receiving this command for an unsupported Grouping Identifier SHOULD return information
relating to Grouping Identifier 1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 611




<!-- PAGE 613 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.8.5** **Association** **Group** **Name** **Report**


This command is used to advertise the assigned name of an association group.


Table 3.30: Association Group Name Report

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|
|Command = ASSOCIATION_GROUP_NAME_REPORT<br>|Command = ASSOCIATION_GROUP_NAME_REPORT<br>|Command = ASSOCIATION_GROUP_NAME_REPORT<br>|Command = ASSOCIATION_GROUP_NAME_REPORT<br>|Command = ASSOCIATION_GROUP_NAME_REPORT<br>|Command = ASSOCIATION_GROUP_NAME_REPORT<br>|Command = ASSOCIATION_GROUP_NAME_REPORT<br>|Command = ASSOCIATION_GROUP_NAME_REPORT<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|Name Length|Name Length|Name Length|Name Length|Name Length|Name Length|Name Length|Name Length|
|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|
|…|…|…|…|…|…|…|…|
|Name N|Name N|Name N|Name N|Name N|Name N|Name N|Name N|



**Grouping** **Identifier** **(1** **byte)**

This field is used to advertise the actual association group identifier.


**Name** **Length** **(1** **byte)**

CC:0059.01.02.11.001 This field indicates the length in bytes of the Name field. The value MUST be in the range 0..42.


**Name** **(N** **bytes)**

This field is used to indicate the assigned name for the actual Group Identifier.

CC:0059.01.02.11.002 The length of this field in bytes MUST comply with the advertised value in the Name Length field.


CC:0059.01.02.11.003 The string MUST NOT contain any appended termination characters.


CC:0059.01.02.11.004 The characters MUST be encoded in UTF-8 format.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 612




<!-- PAGE 614 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.8.6** **Association** **Group** **Info** **Get**


This command is used to request the properties of one or more association group.


CC:0059.01.03.11.001 The Association Group Info Report MUST be returned in response to this command.


CC:0059.01.03.11.002 This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.31: Association Group Info Get

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|
|Command = ASSOCIATION_GROUP_INFO_GET|Command = ASSOCIATION_GROUP_INFO_GET|Command = ASSOCIATION_GROUP_INFO_GET|Command = ASSOCIATION_GROUP_INFO_GET|Command = ASSOCIATION_GROUP_INFO_GET|Command = ASSOCIATION_GROUP_INFO_GET|Command = ASSOCIATION_GROUP_INFO_GET|Command = ASSOCIATION_GROUP_INFO_GET|
|Refresh cache|List<br>Mode|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|



**List** **Mode** **(1** **bit)**

This field is used to request the properties of the supported association groups of a node.

CC:0059.01.03.11.003 If List Mode is set to 1, a receiving node MUST ignore the Grouping Identifier field and return the

CC:0059.01.03.13.001 properties of all its supported associations groups. The receiving node MAY return the response in
several Reports, (e.g. due to memory constraints or a high number of association groups).


CC:0059.01.03.11.004 If List Mode is set to 0, a receiving node MUST advertise the properties of the association group
identified by the Grouping Identifier.


CC:0059.01.03.11.005 The Association Group Info Report returned in response to this command MUST advertise the same
List Mode value as specified by this field.


**Refresh** **Cache** **(1** **bit)**


CC:0059.01.03.11.006 If AGI information is transferred via a gateway, the gateway MUST cache information for all nodes;
also listening nodes.

The AGI Get command flag “Refresh Cache” is used by a management application to instruct a
gateway to update its cache on the first chance given. In case of a sleeping device, this may require
a user operation to wake up the device. In case of a Wake Up device, the gateway may wait for the
next Wake Up Notification from the actual device.


CC:0059.01.03.11.007 The “Refresh Cache” value 0 MUST specify that the gateway is to return its cached information.


CC:0059.01.03.11.008 The “Refresh Cache” value 1 MUST specify that the gateway is to return its cached information and
update its cache on the first chance given.


CC:0059.01.03.12.001 The “Refresh Cache” SHOULD be set to 0 by a sending node.

A receiving node may have re-configurable AGI properties, e.g. if it is a configurable multi-purpose
CC:0059.01.03.13.002 remote control. If the “Dynamic Info” flag of the AGI Report command is set to 1, a sending node
MAY set the “Refresh Cache” flag in the AGI Get command to force the gateway to update its cache,
e.g. after the sending node has re-configured the AGI properties of the receiving node.


**Reserved**

CC:0059.01.03.11.009 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.

**Grouping** **Identifier** **(1** **byte)**

CC:0059.01.03.11.00A This field is used to specify the requested association group identifier. This value MUST be ignored
if the List Mode field is set to 1.

CC:0059.01.03.12.002 A node receiving this command for an unsupported Grouping Identifier SHOULD return information
relating to Grouping Identifier 1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 613




<!-- PAGE 615 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.8.7** **Association** **Group** **Info** **Report**


This command is used to advertise the properties of one or more association groups.


Table 3.32: Association Group Info Report

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|
|Command = ASSOCIATION_GROUP_INFO_REPORT|Command = ASSOCIATION_GROUP_INFO_REPORT|Command = ASSOCIATION_GROUP_INFO_REPORT|Command = ASSOCIATION_GROUP_INFO_REPORT|Command = ASSOCIATION_GROUP_INFO_REPORT|Command = ASSOCIATION_GROUP_INFO_REPORT|Command = ASSOCIATION_GROUP_INFO_REPORT|Command = ASSOCIATION_GROUP_INFO_REPORT|
|List mode|Dynamic<br>Info|Group Count<br>|Group Count<br>|Group Count<br>|Group Count<br>|Group Count<br>|Group Count<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|Mode = 0<br>|Mode = 0<br>|Mode = 0<br>|Mode = 0<br>|Mode = 0<br>|Mode = 0<br>|Mode = 0<br>|Mode = 0<br>|
|Profle MSB<br>|Profle MSB<br>|Profle MSB<br>|Profle MSB<br>|Profle MSB<br>|Profle MSB<br>|Profle MSB<br>|Profle MSB<br>|
|Profle LSB|Profle LSB|Profle LSB|Profle LSB|Profle LSB|Profle LSB|Profle LSB|Profle LSB|
|Reserved = 0|Reserved = 0|Reserved = 0|Reserved = 0|Reserved = 0|Reserved = 0|Reserved = 0|Reserved = 0|
|Event Code MSB = 0|Event Code MSB = 0|Event Code MSB = 0|Event Code MSB = 0|Event Code MSB = 0|Event Code MSB = 0|Event Code MSB = 0|Event Code MSB = 0|
|Event Code LSB = 0|Event Code LSB = 0|Event Code LSB = 0|Event Code LSB = 0|Event Code LSB = 0|Event Code LSB = 0|Event Code LSB = 0|Event Code LSB = 0|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|Mode = 0<br>|Mode = 0<br>|Mode = 0<br>|Mode = 0<br>|Mode = 0<br>|Mode = 0<br>|Mode = 0<br>|Mode = 0<br>|
|Profle MSB<br>|Profle MSB<br>|Profle MSB<br>|Profle MSB<br>|Profle MSB<br>|Profle MSB<br>|Profle MSB<br>|Profle MSB<br>|
|Profle LSB|Profle LSB|Profle LSB|Profle LSB|Profle LSB|Profle LSB|Profle LSB|Profle LSB|
|Reserved = 0|Reserved = 0|Reserved = 0|Reserved = 0|Reserved = 0|Reserved = 0|Reserved = 0|Reserved = 0|
|Event Code MSB = 0|Event Code MSB = 0|Event Code MSB = 0|Event Code MSB = 0|Event Code MSB = 0|Event Code MSB = 0|Event Code MSB = 0|Event Code MSB = 0|
|Event Code LSB = 0|Event Code LSB = 0|Event Code LSB = 0|Event Code LSB = 0|Event Code LSB = 0|Event Code LSB = 0|Event Code LSB = 0|Event Code LSB = 0|



**List** **Mode** **(1** **bit)**

CC:0059.01.04.11.001 The List Mode field MUST advertise the same value as specified in the Association Group Info Get
command which caused this command to be returned.


CC:0059.01.04.13.001 If List Mode is 1, a sending node is advertising the properties of all association groups. The sending
node MAY return several Reports.


CC:0059.01.04.11.002 If List Mode is 0 a sending node MUST advertise the properties of one association group.


**Dynamic** **Info** **(1** **bit)**

CC:0059.01.04.13.002 If the Dynamic Info field is set to 1, the information MAY change and a controlling node SHOULD

CC:0059.01.04.11.003 perform periodic cache refresh for this node. Nodes MUST set this bit if they are able to change the
Association Group Information on the fly.

CC:0059.01.04.11.004 If this field is set to 0, a controlling node MUST NOT request this information more than one time.


**Group** **Count** **(6** **bits)**

CC:0059.01.04.11.005 This field indicates the number of association groups advertised in the command. The Grouping
Identifier, Mode, Profile, Reserved and Event Code fields MUST be repeated for each association

group.

CC:0059.01.04.11.006 If List Mode is set to 0, the Group Count field MUST be set to 1.

If List Mode is set to 1, the Group Count field MUST advertise the number of association group
property blocks following this field.


A node receiving this report may determine the total number of association groups via the Association
Supported Groupings Get or Multi Channel Association Supported Groupings Get commands.

**Grouping** **Identifier** **(1** **byte)**

CC:0059.01.04.11.007 This field MUST advertise the association group identifier of the actual association group property
block.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 614




<!-- PAGE 616 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Mode** **(1** **byte)**

CC:0059.01.04.11.008 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.

**Profile** **(2** **bytes)**

This field is used to advertise the profile of the actual association group. Refer to Section 3.2.8.3.2
CC:0059.01.04.11.009 and Table 3.36. This field MUST be encoded according to Table 3.36.


**Reserved**

CC:0059.01.04.11.00A This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Event** **Code** **(2** **bytes)**

CC:0059.01.04.11.00B This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 615




<!-- PAGE 617 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.8.8** **Association** **Group** **Command** **List** **Get**


This command is used to request the commands that are sent via a given association group.


CC:0059.01.05.11.001 The Association Group Command List Report MUST be returned in response to this command.


CC:0059.01.05.11.002 This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.33: Association Group Command List Get

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|
|Command = ASSOCIATION_GROUP_COMMAND_LIST_GET|Command = ASSOCIATION_GROUP_COMMAND_LIST_GET|Command = ASSOCIATION_GROUP_COMMAND_LIST_GET|Command = ASSOCIATION_GROUP_COMMAND_LIST_GET|Command = ASSOCIATION_GROUP_COMMAND_LIST_GET|Command = ASSOCIATION_GROUP_COMMAND_LIST_GET|Command = ASSOCIATION_GROUP_COMMAND_LIST_GET|Command = ASSOCIATION_GROUP_COMMAND_LIST_GET|
|Allow cache|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|



**Allow** **Cache** **(1** **bit)**

This field indicates that a Z-Wave Gateway device is allowed to intercept the request and return a
cached response on behalf of the specified target.

CC:0059.01.05.11.003 If this bit is not set to 1, a Z-Wave Gateway device MUST forward the request to the specified target.


CC:0059.01.05.12.001 A requesting node SHOULD allow caching to save network bandwidth.


CC:0059.01.05.11.004 A Z-Wave Gateway device MUST cache information for all nodes; also listening nodes. This will save
network bandwidth.


A Z-Wave Gateway device MUST forward the request if it does not hold cached information for the
CC:0059.01.05.11.005 specified target. The Z-Wave Gateway device MUST cache the data returned.


**Reserved**

CC:0059.01.05.11.006 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.

**Grouping** **Identifier** **(1** **byte)**

This field is used to specify the requested association group identifier.

CC:0059.01.05.12.002 A node that receives an unsupported Grouping Identifier SHOULD return information relating to
Grouping Identifier 1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 616




<!-- PAGE 618 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.8.9** **Association** **Group** **Command** **List** **Report**


This command is used to advertise the commands that are sent via an actual association group.


Table 3.34: Association Group Command List Report

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|Command Class = COMMAND_CLASS_ASSOCIATION_GRP_INFO|
|Command = ASSOCIATION_GROUP_COMMAND_LIST_REPORT<br>|Command = ASSOCIATION_GROUP_COMMAND_LIST_REPORT<br>|Command = ASSOCIATION_GROUP_COMMAND_LIST_REPORT<br>|Command = ASSOCIATION_GROUP_COMMAND_LIST_REPORT<br>|Command = ASSOCIATION_GROUP_COMMAND_LIST_REPORT<br>|Command = ASSOCIATION_GROUP_COMMAND_LIST_REPORT<br>|Command = ASSOCIATION_GROUP_COMMAND_LIST_REPORT<br>|Command = ASSOCIATION_GROUP_COMMAND_LIST_REPORT<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|List Length|List Length|List Length|List Length|List Length|List Length|List Length|List Length|
|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|
|Command 1|Command 1|Command 1|Command 1|Command 1|Command 1|Command 1|Command 1|
|…|…|…|…|…|…|…|…|
|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|
|Command N|Command N|Command N|Command N|Command N|Command N|Command N|Command N|



**Grouping** **Identifier** **(1** **byte)**

This field is used to advertise the actual association group identifier.


**List** **Length** **(1** **byte)**

This field advertises the length in bytes of the command list (Command Class and Command fields).


**Command** **Class** **and** **Command**


CC:0059.01.06.13.001 Command Classes MAY be normal or extended Command Classes.


Normal Command Classes are represented as one byte while extended Command Classes are represented as two bytes. Thus, a command list entry (command class + command) is either 2 or 3 bytes
long.


The receiving node must parse individual command list entries to determine if the individual Command
Class is a normal or an extended Command Class.

The first byte of normal command classes is in the range 0x20 – 0xEE, while the first byte of extended
command classes is in the range 0xF1 – 0xFF.

CC:0059.01.06.11.001 A sending node MUST NOT add any command payload in this field.


CC:0059.01.06.11.002 Command Classes already containing destination NodeID such as Wake Up Command Class MUST
NOT be listed in the Association Group Command List Report. This also means that the Wake Up
Command Class MUST NOT be covered by the Lifeline association group.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 617

---

<!-- PAGE 619 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.9** **Association** **Group** **Information** **(AGI)** **Command** **Class,** **version** **2**


The Association Group Information (AGI) Command Class allows a node to advertise the capabilities
of each association group supported by a given application resource.


**3.2.9.1** **Compatibility** **considerations**


The Association Group Information (AGI) Command Class, version 2 introduces the Profile category
“Meter”.

The Association Group Information (AGI) Command Class, version 2 defines no new command fields
or changes to the interpretation of Association Group Information (AGI) Command Class, version 1.


All sections and commands not described in this version remain unchanged from version 1.


**3.2.9.2** **The** **Association** **Group** **Information**


CC:0059.02.00.13.001 A device MAY implement one or more association groups. If the device implements association groups,

CC:0059.02.00.12.001 the device SHOULD provide an Association Group Information (AGI) table as described in in Table
3.25.


**3.2.9.2.1** **Profile**


The profile identifiers are referenced in Table 3.36. The profiles category “Meter” introduced in version
2 is described in Section 3.2.9.2.2.


**3.2.9.2.2** **Meter** **profiles**


“Meter” profiles are intended for association groups of which commands are triggered by meter readings. As an example, a two-phase meter product could comprise three electric meters: one for each
phase and one for the total consumption.

Meter profile identifiers are constructed by prepending the Meter Command Class identifier (referred
to with AGI_PROFILE_METER) to a meter type defined in the Meter Command Class. The values
in Table 8 only serve as examples to illustrate the construction of AGI Meter Profile identifiers. For
the full list of available meter types, refer to the Meter Command Class.


CC:0059.02.00.12.002 In case of multiple logical functions in a device, the device SHOULD implement one Multi Channel
End Point for each logical function; e.g. each meter instance. Table 7 gives an example of a Multi
Channel Meter device with two normal and one aggregated meter functions.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 618




<!-- PAGE 620 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024






























































|Table 3.35: Example AGI Tables for Three-Function Meter Root Device:|Col2|Col3|Col4|
|---|---|---|---|
|Root Device:<br>|Root Device:<br>|Root Device:<br>|Root Device:<br>|
|**Group**<br>**identifer**|**Profle 2**<br>**bytes**|**Command Class & Command**<br>**(list) N bytes**|**Group Name (UTF-8)**<br>**M bytes**|
|1|General:<br>Lifeline|Meter Report<br>Device Reset Locally Notifcation|Lifeline<br>|
|2|Meter:Elec-<br>tric|Basic Set|On/Of control (Phase 1)<br>|
|3|Meter:Elec-<br>tric|Basic Set|On/Of control (Phase 1)<br>|
|4|Meter:Elec-<br>tric|Basic Set|On/Of control (Total<br>Consumption)|
|End Point 1:<br>|End Point 1:<br>|End Point 1:<br>|End Point 1:<br>|
|**Group**<br>**identifer**|**Profle 2**<br>**bytes**|**Command Class & Command**<br>**(list) N bytes**|**Group Name (UTF-8)**<br>**M bytes**|
|1|Meter:Elec-<br>tric|Meter Report|Phase 1 via Lifeline<br>|
|2|Meter:Elec-<br>tric|Basic Set|On/Of control (Phase 1)|
|End Point 2:<br>|End Point 2:<br>|End Point 2:<br>|End Point 2:<br>|
|**Group**<br>**identifer**|**Profle 2**<br>**bytes**|**Command Class & Command**<br>**(list) N bytes**|**Group Name (UTF-8)**<br>**M bytes**|
|1|Meter:Elec-<br>tric|Meter Report|Phase 1 via Lifeline<br>|
|2|Meter:Elec-<br>tric|Basic Set|On/Of control (Phase 1)|
|End Point 3 (aggregated):<br>|End Point 3 (aggregated):<br>|End Point 3 (aggregated):<br>|End Point 3 (aggregated):<br>|
|**Group**<br>**identifer**|**Profle 2**<br>**bytes**|**Command Class & Command**<br>**(list) N bytes**|**Group Name (UTF-8)**<br>**M bytes**|
|1|Meter:Elec-<br>tric|Meter Report|Total Consumption via<br>Lifeline<br>|
|2|Meter:Elec-<br>tric|Basic Set|On/Of control (Total<br>Consumption)|



The Profile identifier is Meter:Electric for all End Points but the Group Name allows a user to
determine which End Point and which association group to use in order to configure the phase 2
meter to control an alarm lamp.


The Root Device in the above example advertises the Meter Report Command in the Lifeline group.
Residing in a Multi Channel device, the Root Device does not actually implement any application
functionality. The Meter Report command is a feature of the End Points which is advertised for
backwards compatibility with legacy devices not supporting the Multi Channel Command Class.


Likewise, the Root device advertises the Basic Set Command in association groups 2..4. This is also
a feature of the End Points. Refer to the Multi Channel Command Class for details on backwards

compatibility.


End Points 1..3 in the above example advertise the Meter Report Command in association group 1.
By advertising that zero NodeIDs are supported for association group 1, End Points indicate that this
command is sent via the Root Device Lifeline group if a Multi Channel association is created for the
Root Device Lifeline group.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 619

---

<!-- PAGE 621 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.10** **Association** **Group** **Information** **(AGI)** **Command** **Class,** **version** **3**


The Association Group Information (AGI) Command Class allows a node to advertise the capabilities
of each association group supported by a given application resource.


**3.2.10.1** **Compatibility** **considerations**


The Association Group Information (AGI) Command Class, version 3 introduces the Profile category
“Irrigation”.

The Association Group Information (AGI) Command Class, version 3 defines no new command fields
or changes to the interpretation of Association Group Information (AGI) Command Class, version 1
and version 2.


All sections and commands not described in this version remain unchanged from version 2.


**3.2.10.2** **The** **Association** **Group** **Information**


A node may implement one or more association groups. If the device implements association groups,
CC:0059.03.00.12.001 the device SHOULD provide an Association Group Information (AGI) table as described in Table
3.25


**3.2.10.2.1** **Profile**


The profile categories are referenced in Table 3.36. The profiles category “Irrigation” introduced in
version 3 is described in Section 3.2.10.2.2.


**3.2.10.2.2** **Irrigation** **Profiles**


“Irrigation” profiles are intended for association groups of which commands are triggered by irrigation
events. As an example, an irrigation control device may provide 8 channels that can each control an
external resource such as a valve or a pump.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 620




<!-- PAGE 622 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024












































|Profile|Table 3.36: AGI Profiles Explanation|Profile identifier|Col4|
|---|---|---|---|
|**Profle**|**Explanation**|**Profle identifer**|**Profle identifer**|
|||**MSB**|**LSB**|
|Gen-<br>eral:NA<br>(v1)|“Not Applicable”<br>There is no specifc class of events for this<br>association group|AGI_PRO-<br>FILE_GEN-<br>ERAL =<br>0x00|AGI_GEN-<br>ERAL_NA =<br>0x00|
|General:<br>Lifeline<br>(v1)|“Lifeline”<br>This association group is intended for all events<br>relevant for the Lifeline group|AGI_PRO-<br>FILE_GEN-<br>ERAL =<br>0x00|AGI_GEN-<br>ERAL_LIFE-<br>LINE =<br>0x01|
|||||
|Con-<br>trol:Key01<br>(v1)|“Control Key 1”<br>Members of this association group are controlled<br>or receive reports in response to user input for<br>key 1|AGI_PRO-<br>FILE_CON-<br>TROL =<br>0x20|AGI_CON-<br>TROL_KEY01 =<br>0x01|
|Con-<br>trol:Key<br>xx (v1)|…|…|…|
|Con-<br>trol:Key32<br>(v1)|“Control Key 32”<br>Members of this association group are controlled<br>or receive reports in response to user input for<br>key 32|AGI_PRO-<br>FILE_CON-<br>TROL =<br>0x20|AGI_CON-<br>TROL_KEY32 =<br>0x20|
|||||
|Sensor:<br>Air tem-<br>perature<br>(v1)|“Sensor, Air Temperature”<br>Members of this association group are controlled<br>or receive reports when the sensor value changes|AGI_PRO-<br>FILE_SEN-<br>SOR =<br>0x31|MULTI-<br>LEVEL_SEN-<br>SOR_TYPE_<br>TEMPERA-<br>TURE =<br>0x01|
|Sensor:<br>Humid-<br>ity<br>(v1)|“Sensor, Humidity”<br>Members of this association group are controlled<br>or receive reports when the sensor value changes|AGI_PRO-<br>FILE_SEN-<br>SOR =<br>0x31|MULTI-<br>LEVEL_SEN-<br>SOR_TYPE_<br>HUMIDITY =<br>0x05|
|…|(only examples above.<br>Sensor profles are built based on the Sensor<br>Type as described in Section 3.2.8.3.5|AGI_PRO-<br>FILE_SEN-<br>SOR =<br>0x31|MULTI-<br>LEVEL_SEN-<br>SOR_TYPE_<br>TEMPERA-<br>TURE =<br>0x01|
|||||
|Notifca-<br>tion:<br>Smoke<br>Alarm<br>(v1)<br>|“Notifcation, Smoke Alarm”<br>Members of this association group are controlled<br>or receive reports when an event or state change<br>is detected.for the given Notifcation Type<br>|AGI_PRO-<br>FILE_<br>NOTIFICA-<br>TION =<br>0x71|NOTIFICA-<br>TION_TYPE_<br>SMOKE = 0x01|
|Notifca-<br>tion:<br>C02<br>Alarm<br>(v1)|“Notifcation, CO2 Alarm”<br>Members of this association group are controlled<br>or receive reports when an event or state change<br>is detected.for the given Notifcation Type|AGI_PRO-<br>FILE_<br>NOTIFICA-<br>TION =<br>0x71|NOTIFICA-<br>TION_TYPE_<br>CO2 = 0x03|
|…|(only examples above.<br>Notifcation profles are built based on the<br>Notifcation Type as described in Section<br>3.2.8.3.6.|AGI_PRO-<br>FILE_NO-<br>TIFICA-<br>TION =<br>0x71|…|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 621




<!-- PAGE 623 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 3.37: AGI Profiles Continued




















|i<br>Profle|Explanation|i i<br>Profle identifer|Col4|
|---|---|---|---|
|||**MSB**|**LSB**|
|Meter:<br>Electric,<br>kWH<br>(v2)|“Meter, Electric”<br>Members of this association group receive<br>meter reports or are controlled when a<br>metering event is detected.|AGI_PRO-<br>FILE_ME-<br>TER =<br>0x32|METER_TYPE_<br>ELECTRIC = 0x01|
|Meter:<br>Gas (v2)|“Meter, Gas”<br>Members of this association group receive<br>meter reports or are controlled when a<br>metering event is detected.|AGI_PRO-<br>FILE_ME-<br>TER =<br>0x32|METER_TYPE_<br>GAS = 0x02|
|Meter:<br>Water<br>(v2)|“Meter, Water”<br>Members of this association group receive<br>meter reports or are controlled when a<br>metering event is detected.|AGI_PRO-<br>FILE_ME-<br>TER =<br>0x32|METER_TYPE_<br>WATER = 0x03|
|…|(only examples above.<br>Meter profles are built based on the<br>Notifcation Type as described in Section<br>3.2.9.2.2.|AGI_PRO-<br>FILE_ME-<br>TER =<br>0x32|MULTI-<br>LEVEL_SEN-<br>SOR_TYPE_<br>TEMPERATURE =<br>0x01|
|||||
|Irriga-<br>tion:<br>Channel<br>01 (v3)|“Irrigation Channel 01”<br>Member(s) of this association group are<br>controlled by channel 1 of an irrigation<br>control device|AGI_PRO-<br>FILE_IRRI-<br>GATION =<br>0x6B|AGI_IRRIGA-<br>TION_CHANNEL_<br>01 = 0x01|
|Irriga-<br>tion:<br>Channel<br>xx (v3)|…|…|…|
|Irriga-<br>tion:|“Irrigation Channel 32”<br>Members of this association group are<br>controlled or receive reports in response to<br>user input for key 32|AGI_PRO-<br>FILE_IRRI-<br>GATION =<br>0x6B|AGI_IRRIGA-<br>TION_CHANNEL_<br>32 = 0x20|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 622