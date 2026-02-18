<!-- PAGE 124 -->

CC:005B.01.00.11.001



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.22** **Central** **Scene** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **OBSOLETED**


New implementations MUST support the Central Scene Command Class, version 3 or newer.


The Central Scene Command Class is used to communicate central scene activations to a central controller using the lifeline concept. The central scene controller only need to configure lifeline association
in relevant nodes before the home control application can take action in the central scene controller.
The typical application contains up to 10-15 selected nodes creating a nice “out of the box” experience
with minimum effort by the customer. A scene is typically activated via a push button on the device
in question.


The Central Scene Command Class can instruct the central scene controller to perform the relevant
actions as shown on Figure 2.6.


Figure 2.6: Centralized feedback and control



CC:005B.01.00.13.001 Multiple sending nodes MAY advertise the same Scene number.


Therefore, a receiving node MUST interpret the advertised Scene number in combination with the
source NodeID of the sending node.


For instance, {Node A, Scene 1} may trigger changes to another scene than {Node B, Scene 1} in the
receiving node

Notice that this configuration has a single point of failure in case the central scene controller is broken.
The likelihood to experience the “popcorn effect” is increased because the central scene controller may
be located far from the push button activated and therefore out of direct range with respect to devices
to control.


To compensate for single point of failure in case the central scene controller is broken the devices could
do fallback to alternative association groups to control devices directly. These association groups are
activated only if the device does not receive acknowledge from configured lifeline. This will ensure
some basic level of light control in the house until the central scene controller is restored. Alternatively,
a backup central scene controller could be added to the system to take over in case the first one fails.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 123




<!-- PAGE 125 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.22.1** **Central** **Scene** **Supported** **Get** **Command**


This command is used to request the maximum number of scenes that this device supports.


CC:005B.01.01.11.001 The Central Scene Supported Report Command MUST be returned in response to this command.


CC:005B.01.01.11.002 This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.106: Central Scene Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|
|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|



**2.2.22.2** **Central** **Scene** **Supported** **Report** **Command**


This command is used to report the maximum number of scenes that the requested device supports.


Table 2.107: Central Scene Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|
|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|
|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|



**Supported** **Scenes** **(8** **bits)**

This field indicates the maximum number of scenes supported by the requested device.

CC:005B.01.02.11.001 This field MUST advertise the number of available scenes.


Scenes MUST be numbered in the range 1..[Supported Scenes].


CC:005B.01.02.13.001 A device MAY implement virtual buttons via two-button presses, touch screen swipes or other means.


CC:005B.01.02.11.002 Virtual buttons MUST be numbered after physical push buttons or graphical button objects.


CC:005B.01.02.11.003 The advertised number of Supported Scenes MUST cover physical push buttons, graphical button

CC:005B.01.02.13.002 objects as well as virtual buttons. Therefore, the advertised number of Supported Scenes MAY be
larger than the number of physical push buttons or graphical button objects.


**2.2.22.3** **Central** **Scene** **Notification** **Command**


This command is used to report activated scene on device in question including how notification must
be interpreted.

In case a lifeline is configured in group #1 using Association Command Class, the device must use
this lifeline for transmitting the Central Scene Notification Command. It is allowed to define other
association groups handling Central Scene Notification Command and setup rules between the groups.
However, lifeline has precedence over other groups handling Central Scene Notification Command in
case lifeline is defined.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 124




<!-- PAGE 126 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.108: Central Scene Notification Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|
|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|
|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|
|Reserved|Reserved|Reserved|Reserved|Reserved|Key Attributes|Key Attributes|Key Attributes|
|Scene Number|Scene Number|Scene Number|Scene Number|Scene Number|Scene Number|Scene Number|Scene Number|



**Sequence** **Number** **(8** **bits)**

CC:005B.01.03.11.001 The sequence number MUST be incremented each time a Central Scene Notification Command is
issued. The receiving device uses the sequence number to ignore duplicates.


**Key** **Attributes** **(3** **bits)**

CC:005B.01.03.11.002 The key Attributes field specifies the state of the key. The field MUST be encoded according to Table
2.109


Table 2.109: Central Scene Notification::Key Attributes

|Key Attribute|Description|
|---|---|
|0x00|Key Pressed|
|0x01|Key Released|
|0x02|Key Held Down|



CC:005B.01.03.11.003 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

CC:005B.01.03.11.004 Notifications carrying these Key Attributes MUST comply with Figure 2.7


Figure 2.7: Central Scene version 1 button press decoding and timer management


**Reserved**

CC:005B.01.03.11.005 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Scene** **Number** **(8** **bits)**


CC:005B.01.03.11.006 The advertised number of Supported Scenes MUST cover physical push buttons, graphical button

CC:005B.01.03.13.001 objects as well as virtual buttons. Therefore, the advertised number of Supported Scenes MAY be
larger than the number of physical push buttons or graphical button objects.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 125




<!-- PAGE 127 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 2.8: Scene number mapping to button layout


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 126

---

<!-- PAGE 128 -->

CC:005B.02.00.11.001



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.23** **Central** **Scene** **Command** **Class,** **version** **2** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **OBSOLETED**


New implementations MUST support the _Central_ _Scene_ _Command_ _Class,_ _version_ _3_ or newer.


The Central Scene Command Class is used to communicate central scene activations to a central

controller using the lifeline concept.


**2.2.23.1** **Compatibility** **considerations**


Central Scene Command Class version 2 is extended on the following areas:


 - The Central Scene Supported Report Command is updated to advertise Key Attributes support
for each scene.

 - Additional Key Attributes are defined.


Commands and paragraphs not mentioned in this version remain unchanged from version 1.


**2.2.23.2** **Central** **Scene** **Supported** **Report** **Command**


This command is used to report the maximum number of supported scenes and the Key Attributes
supported for each scene.


Table 2.110: Central Scene Supported Report Command, version

|7|Table 2 6|2.110: Cen 5|ntral Scene 4|e Supported 3|d Report Comma 2|and, version 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|
|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|
|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|
|Reserved|Reserved|Reserved|Reserved|Reserved|Number of Bit Mask Bytes|Number of Bit Mask Bytes|Identical|
|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|
|…|…|…|…|…|…|…|…|
|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|
|…|…|…|…|…|…|…|…|
|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|
|…|…|…|…|…|…|…|…|
|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|



Fields not described below remain unchanged from version 1.


**Reserved**



CC:005B.02.02.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Number** **of** **Bit** **Mask** **Bytes** **(2** **bits)**

This field advertises the size of each “Supported Key Attributes” field measured in bytes.


The value MUST be in the range 1..3.

CC:005B.02.02.11.002

**Identical** **(1** **bit)**

This field indicates if all scenes are supporting the same Key Attributes:


CC:005B.02.02.11.003 The value 1 MUST indicate that all scenes support the same set of Key Attributes. In this case, the
field “Supported Key Attributes for Scene 1” MUST advertise the supported Key Attributes for all

scenes


CC:005B.02.02.11.004


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 127




<!-- PAGE 129 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value 0 MUST indicate that scenes support different Key Attributes. In this case, Supported
Key Attributes MUST be advertised for each individual scene.


**Supported** **Key** **Attributes** **(N** **bytes)**

CC:005B.02.02.11.005 This Bit Mask field advertises the attributes supported by the corresponding scene. The field MUST
be encoded according to Table 2.111


Table 2.111: Central Scene Supported Report::Supported Key At
|Table 2. tributes Byte:Bit|.111: Central Scene Supported Report::Supported Key At- Supported Key Attributes|
|---|---|
|Byte:Bit|Supported Key Attributes|
|1:0|Key Pressed 1 time|
|1:1|Key Released.|
|1:2|Key Held Down.|
|1:3|Key Pressed 2 times|
|1:4|Key Pressed 3 times|
|1:5|Key Pressed 4 times|
|1:6|Key Pressed 5 times|
|1:7|Reserved|



CC:005B.02.02.11.006 If the Key Released attribute is supported, the Key Held Down attribute MUST also be supported.


If the Key Held Down attribute is supported, the Key Released attribute MUST also be supported.


**2.2.23.3** **Central** **Scene** **Notification** **Command**


This command is used to advertise one or more key events.


If the device implements Z-Wave Plus Lifeline support is implemented, the device MUST send the
Central Scene Notification Command to the actual Lifeline targets.


Table 2.112: Central Scene Notification Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|
|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|
|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|
|Reserved|Reserved|Reserved|Reserved|Reserved|Key Attributes|Key Attributes|Key Attributes|
|Scene Number|Scene Number|Scene Number|Scene Number|Scene Number|Scene Number|Scene Number|Scene Number|



Fields not described below remain unchanged from version 1.


**Key** **Attributes** **(3** **bits)**

CC:005B.02.03.11.002 This field advertises one or more events detected by the key. The field MUST be encoded according
to Table 2.113


CC:005B.02.03.11.003

|Key Attribute|Table 2.113: Central Scene Notification::Key Attributes Description|Version|
|---|---|---|
|Key Attribute|Description|Version|
|0x00|Key Pressed|1|
|0x01|Key Released|1|
|0x02|Key Held Down|1|
|0x03|Key Pressed 2 times|2|
|0x04|Key Pressed 3 times|2|
|0x05|Key Pressed 4 times|2|
|0x06|Key Pressed 5 times|2|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 128




<!-- PAGE 130 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

CC:005B.02.03.11.004 Notification carrying these Key Attributes MUST comply with Figure 2.9


Figure 2.9: Central Scene button press decoding and timer management


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 129

---

<!-- PAGE 131 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.24** **Central** **Scene** **Command** **Class,** **version** **3**


The Central Scene Command Class, version 3 extends version 2 by adding a new mode for the
transmission of Key Held Down notifications. This allows a node to send Key Held Down refreshes at
a low rate for the duration of the key held down.


The purpose of this new feature is to provide improved compatibility with FLiRS beaming and network
routing.


Central Scene Command Class, version 3 introduces three new commands to allow a controller to
query and configure node capabilities.

      - Central Scene Configuration Set Command

      - Central Scene Configuration Get Command

      - Central Scene Configuration Report Command


Central Scene Command Class, version 3 extends the following commands for a scene launching node
to advertise its optional capabilities.


      - Central Scene Supported Report Command

      - Central Scene Notification Command


**2.2.24.1** **Compatibility** **considerations**


CC:005B.03.00.22.001 A scene controller SHOULD NOT try to detect multiple key presses from the reception of successive
key press notifications in any single or multiple key attribute combination. FLiRS beaming, collisions
or routing may add delays between messages and render the timing between notifications unreliable.

Version 1 and version 2 required to send Key Held Down notifications commands every 200ms. It has
been found that this requirement cannot be observed when the network is using FLiRS beaming or
routing. Further, issuing the 200ms refreshes also degrades general network reliability and availability.


Version 3 introduces the Slow Refresh Capability, which allows a node to send refreshes every 55
seconds instead of 200ms. For details about the Slow Refresh capability, refer to Section 2.2.24.7.


CC:005B.03.00.21.001 In order to ensure a functioning network, the Slow Refresh capability MUST be enabled by default
after inclusion.


CC:005B.03.00.22.002 When creating associations from a version 3 node, the node creating the association SHOULD enable
the Slow Refresh capability in the node if the association destination does also support Central Scene
Command Class, version 3. When using the version 3 Slow Refresh capability, the controller relies on
the reception of a Key Up notification instead of the Key Held Down refreshes. The new mode still
sends refreshes at a low rate, for the controller to detect if a node failed after sending a Held Down
Key notification. This means that a version 2 controlling node may time out when receiving Key Held
Down Notifications from a version 3 node.


However, it has been found that there exist nodes supporting version 1 or version 2 which do not send
Central Scene Notification refreshes every 200ms when the Key Held Down notification is issued.


CC:005B.03.00.22.003 A controller SHOULD apply an adaptive approach based on the reception of the Key Released Notification. Initially, the controller SHOULD time out if not receiving any Key Held Down Notification
refresh after 400ms and consider this to be a Key Up Notification. If, however, the controller subsequently receives a Key Released Notification, the controller SHOULD consider the sending node to
be operating with the Slow Refresh capability enabled.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 130




<!-- PAGE 132 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.24.1.1** **Central** **Scene** **Configuration** **commands** **support**


If a node supports Slow Refresh Capability (that allows a node to send refresh every 55 seconds instead
of 200 ms), may not allow users to turn off the ‘Slow Refresh’ functionality. If this is the case, the
node MAY choose to ignore the Central Scene Configuration Set Command with ‘Slow Refresh’ bit
set to zero.

If the node chooses to ignore the Central Scene Configuration Set Command, the node MUST return
an application Reject Request Command when receiving Central Scene Configuration Set command
(if it received without Supervision encapsulation).


**2.2.24.1.2** **Multi** **Channel** **considerations**


CC:005B.03.00.22.004 Multi Channel End Points SHOULD NOT support the Central Scene Command Class.


**2.2.24.2** **Central** **Scene** **Configuration** **Set** **Command**


This command is used to configure the use of optional node capabilities for scene notifications.


Table 2.114: Central Scene Configuration Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|
|Command = CENTRAL_SCENE_CONFIGURATION_SET|Command = CENTRAL_SCENE_CONFIGURATION_SET|Command = CENTRAL_SCENE_CONFIGURATION_SET|Command = CENTRAL_SCENE_CONFIGURATION_SET|Command = CENTRAL_SCENE_CONFIGURATION_SET|Command = CENTRAL_SCENE_CONFIGURATION_SET|Command = CENTRAL_SCENE_CONFIGURATION_SET|Command = CENTRAL_SCENE_CONFIGURATION_SET|
|Slow Refresh|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|



**Slow** **Refresh** **(1** **bit)**

This flag is used to configure the use of the Slow Refresh capability.


CC:005B.03.04.11.001 The value 1 MUST indicate that the scene launching node MUST use Slow Refresh.


The value 0 MUST indicate that the scene launching node MUST NOT use Slow Refresh.


**Reserved**

CC:005B.03.04.11.002 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**2.2.24.3** **Central** **Scene** **Configuration** **Get** **Command**


This command is used to query the configuration of optional node capabilities for scene notifications.


CC:005B.03.05.11.001
The Central Scene Configuration Report Command MUST be returned in response to this command.


CC:005B.03.05.11.002 This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.115: Central Scene Configuration Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|
|Command = CENTRAL_SCENE_CONFIGURATION_GET|Command = CENTRAL_SCENE_CONFIGURATION_GET|Command = CENTRAL_SCENE_CONFIGURATION_GET|Command = CENTRAL_SCENE_CONFIGURATION_GET|Command = CENTRAL_SCENE_CONFIGURATION_GET|Command = CENTRAL_SCENE_CONFIGURATION_GET|Command = CENTRAL_SCENE_CONFIGURATION_GET|Command = CENTRAL_SCENE_CONFIGURATION_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 131




<!-- PAGE 133 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.24.4** **Central** **Scene** **Configuration** **Report** **Command**


This command is used to advertise the configuration of optional node capabilities for scene notifications.


Table 2.116: Central Scene Configuration Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|
|Command = CENTRAL_SCENE_CONFIGURATION_REPORT|Command = CENTRAL_SCENE_CONFIGURATION_REPORT|Command = CENTRAL_SCENE_CONFIGURATION_REPORT|Command = CENTRAL_SCENE_CONFIGURATION_REPORT|Command = CENTRAL_SCENE_CONFIGURATION_REPORT|Command = CENTRAL_SCENE_CONFIGURATION_REPORT|Command = CENTRAL_SCENE_CONFIGURATION_REPORT|Command = CENTRAL_SCENE_CONFIGURATION_REPORT|
|Slow Refresh|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|



**Slow** **Refresh** **(1** **bit)**

This flag is used to advertise the use of the Slow Refresh capability.


CC:005B.03.06.11.001 The value 1 MUST indicate that the scene launching node MUST use Slow Refresh.


The value 0 MUST indicate that the scene launching node MUST NOT use Slow Refresh capability.


**Reserved**

CC:005B.03.06.11.002 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**2.2.24.5** **Central** **Scene** **Supported** **Get** **Command**


This command is used to request the maximum number of scenes that this device supports.


CC:005B.03.01.11.001 The Central Scene Supported Report Command MUST be returned in response to this command.


CC:005B.03.01.11.002 This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.117: Central Scene Supported Get Command, version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|
|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|Command = CENTRAL_SCENE_SUPPORTED_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 132




<!-- PAGE 134 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.24.6** **Central** **Scene** **Supported** **Report** **Command**


This command is used to report the maximum number of supported scenes and the Key Attributes
supported for each scene.


Table 2.118: Central Scene Supported Report Command, version

|Table 3 7|e 2.118: C 6|Central Sce 5|ene Suppo 4|orted Repo 3|ort Command, 2|version 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|
|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|Command = CENTRAL_SCENE_SUPPORTED_REPORT|
|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|Supported Scenes|
|Slow Refresh<br>Support|Reserved|Reserved|Reserved|Reserved|Number of Bit Mask Bytes|Number of Bit Mask Bytes|Identi-<br>cal|
|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|Supported Key Attributes for Scene 1 - Byte 1|
|…|…|…|…|…|…|…|…|
|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|Supported Key Attributes for Scene 1 - Byte N|
|…|…|…|…|…|…|…|…|
|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|Supported Key Attributes for Scene M - Byte 1|
|…|…|…|…|…|…|…|…|
|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|Supported Key Attributes for Scene M - Byte N|



All fields not described below are the same as in version 2.


**Slow** **Refresh** **Support** **(1** **bit)**

This field indicates whether the node supports the Slow Refresh capability.


CC:005B.03.02.11.001 The value 1 MUST indicate that the node supports the Slow Refresh capability.


The value 0 MUST indicate that the node does not support the Slow Refresh capability.


**2.2.24.7** **Central** **Scene** **Notification** **Command**


This command is used to advertise a key event.


CC:005B.03.03.11.001 If the device implements Z-Wave Plus Lifeline support, the device MUST send the Central Scene
Notification Command to the actual Lifeline targets.


Table 2.119: Central Scene Notification Command, version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|Command Class = COMMAND_CLASS_CENTRAL_SCENE|
|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|Command = CENTRAL_SCENE_NOTIFICATION|
|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|
|Slow Refresh|Reserved|Reserved|Reserved|Reserved|Key Attribute|Key Attribute|Key Attribute|
|Scene Number|Scene Number|Scene Number|Scene Number|Scene Number|Scene Number|Scene Number|Scene Number|



All fields not described below are the same as in version 2.


**Slow** **Refresh** **(1** **bit)**

This flag is used to advertise if the node is sending Key Held Down notifications at a slow rate. A
CC:005B.03.03.11.002 sending node MUST always set this field according to the configured mode.

CC:005B.03.03.11.003 A receiving node MUST ignore this field if the command is not carrying the Key Held Down key
attribute.

If the Slow Refresh field is 0:

CC:005B.03.03.12.002 - A new Key Held Down notification SHOULD be sent every 200ms until the key is released.

CC:005B.03.03.11.005 - The Sequence Number field MUST be updated at each notification transmission.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 133




<!-- PAGE 135 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


CC:005B.03.03.12.001 - If not receiving a new Key Held Down notification within 400ms, a controlling node SHOULD
use an adaptive timeout approach as described in Section 2.2.24.1.

If the Slow Refresh field is 1:

CC:005B.03.03.11.006 - A new Key Held Down notification MUST be sent every 55 seconds until the key is released.

CC:005B.03.03.11.007 - The Sequence Number field MUST be updated at each notification refresh.



CC:005B.03.03.11.008




 - If not receiving a new Key Held Down notification within 60 seconds after the most recent
Key Held Down notification, a receiving node MUST respond as if it received a Key Release
notification.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 134