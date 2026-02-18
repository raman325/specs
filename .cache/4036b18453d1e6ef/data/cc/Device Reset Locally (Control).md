<!-- PAGE 1144 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.4** **Device** **Reset** **Locally** **Command** **Class,** **version** **1**


**6.3.4.1** **Mandatory** **node** **interview**


No mandatory node interview is required for this Command Class.


**6.3.4.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.3.4.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.3.4.4** **Additional** **control** **requirements**


CL:005A.01.52.01.1 A controlling node receiving the Device Reset Locally Notification Command SHOULD consider
the sending node to be a failing node and accordingly perform relevant maintenance operations like
removing failing nodes, removing associations to failing nodes, etc.

CL:005A.01.51.01.1 A controlling node receiving the Device Reset Locally Notification Command MUST indicate to the
end user that the node has been reset and left the Z-Wave network.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1143




<!-- PAGE 1145 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.5** **Firmware** **Update** **Meta** **Data** **Command** **Class,** **version** **1-6**


**6.3.5.1** **Mandatory** **node** **interview**


CL:007A.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.32.


Figure 6.32: Firmware Update Meta Data Command Class interview


**6.3.5.2** **Minimum** **end** **user** **functionalities**


**6.3.5.2.1** **Firmware** **update**


CL:007A.01.32.01.1 A controlling node SHOULD provide a method for updating the firmware of a supporting node.
The end user SHOULD be able to select a firmware file or ask the controller to look for updates
automatically.


CL:007A.01.31.01.1 If this functionality is available, the issued commands MUST comply with Figure 6.33 when the end
user performs this action.


CL:007A.01.33.01.1 A controlling node MAY use additional commands such as Firmware Update Activation Set Command
for the firmware update.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1144




<!-- PAGE 1146 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 6.33: Firmware Update Meta Data::Firmware Update


CL:007A.01.32.02.1
If a controlling node allows the end user to interrupt an ongoing firmware update transfer, it SHOULD
issue a FIRMWARE_UPDATE_MD_REPORT Command with the Last field set to 1 prematurely.


**6.3.5.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


CL:007A.01.42.01.1 A controlling node SHOULD have a UI allowing the end user to see the Firmware version of a
supporting node.


**6.3.5.4** **Additional** **control** **requirements**


If the supporting node supports Battery Command Class and the controlling node controls Battery
CL:007A.01.52.01.1 Command Class, the controlling node SHOULD issue a Battery Get and read the battery level before
initiating a Firmware Update.


CL:007A.01.52.02.1 A controlling node SHOULD NOT initiate a Firmware Update if the supporting node Battery level
is less than 50%.

CL:007A.01.51.01.1 A controlling node MUST perform a full interview of a node after performing a firmware update.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1145




<!-- PAGE 1147 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.6** **Indicator** **Command** **Class,** **version** **1-3**


**6.3.6.1** **Mandatory** **node** **interview**


CL:0087.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.34.


Figure 6.34: Indicator Command Class interview


**6.3.6.2** **Minimum** **end** **user** **functionalities**


CL:0087.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1146




<!-- PAGE 1148 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.6.2.1** **Identify**


CL:0087.01.31.02.1 If the supporting and controlling nodes are version 3 or newer, the end user MUST be able to instruct
the node to identify itself. When the end user performs this action, the issued command MUST
comply with Table 6.41.

|Field|Table 6.41: Indicator::Identity Value|
|---|---|
|Field|Value|
|Command|INDICATOR_SET|
|Indicator 0 Value|0x00|
|Indicator object count|0x03|
|Indicator ID 1|0x50|
|Property ID 1|0x03|
|Value 1|0x08|
|Indicator ID 2|0x50|
|Property ID 2|0x04|
|Value 2|0x03|
|Indicator ID 3|0x50|
|Property ID 3|0x05|
|Value 3|0x06|



The supporting node will be switched on 600ms and switched off 200ms three times.


CL:0087.01.33.01.1 A controlling node MAY hide this functionality away from the end user if the supporting node also
supports the Wake Up Command Class.


**6.3.6.3** **Node** **properties**


CL:0087.01.42.01.1 The controlling node SHOULD have a UI allowing the end user to see/access the following properties:


     - Last known Indicators’ state/value (ON/OFF or x%), if any


**6.3.6.4** **Additional** **control** **requirements**


CL:0087.01.51.01.1 A node controlling this command class MUST NOT reuse the identify command for any other purpose
than a node identification application.


CL:0087.01.52.01.3 A node controlling this Command Class SHOULD NOT make a supporting node blink 3 times for
any indication (except when using the Identify Indicator for the Identify purpose).


CL:0087.01.52.02.1 A node controlling this Command Class SHOULD allow the end user to actuate additional indicating

resources.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1147




<!-- PAGE 1149 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.7** **Multi** **Channel** **Association** **Command** **Class,** **version** **2-5**


**6.3.7.1** **Mandatory** **node** **interview**


CL:008E.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.35.


Figure 6.35: Multi Channel Association Command Class interview


CL:008E.01.21.02.2 The lifeline association MUST be an End Point Association (controller NodeID after the
MULTI_CHANNEL_ASSOCIATION_SET_MARKER) if:


     - Both nodes implement Multi Channel Association, version 3 or newer.


     - The supporting node also supports the Multi Channel Command Class.


CL:008E.01.22.01.1 The lifeline association SHOULD be a NodeID association in any other case.


**6.3.7.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


CL:008E.01.31.01.1 A controlling node implementing a UI which allows an end user to establish association between nodes
MUST NOT restrict the end user from establishing associations that are allowed. Refer to Section
6.3.7.4 for allowed associations.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1148




<!-- PAGE 1150 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.7.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.3.7.4** **Additional** **control** **requirements**


If the supporting node also supports Association and the controlling node controls Association, the
CL:008E.01.51.01.1 controlling node MUST NOT interview and control the Association Command Class.


CL:008E.01.51.02.1 A controlling node MUST use the Association Group Information (AGI) Command Class to probe the
commands that a given association group will be sending before creating associations towards other
nodes.


If an association group in a Node A sends one or more controlling commands:


CL:008E.01.51.03.3 - A controlling node MUST NOT associate Node A to a Node B destination that does not support
the Command Class that the Node A will be controlling.


CL:008E.01.53.01.3 - A controlling node MAY create an association to a destination supporting an actuator Command
Class if the actual association group sends Basic Control Command Class.


For Multi Channel Association version 2 and version 3:


CL:008E.02.51.01.1 **–** A controlling node MUST NOT associate Node A to a Node B destination if Node A and
Node B’s highest Security Class are not identical.


For Multi Channel Association version 4 or newer:


CL:008E.04.51.01.1 **–** A controlling node MUST NOT associate Node A to a Node B destination if Node A was
not granted Node B’s highest Security Class.


If an association group sends only supporting commands:


CL:008E.01.53.02.2 - A controlling node MAY create an association to any destination if the actual association group
sends commands reflecting the support of a Command Class by the sending Node/End Point.
Refer to [25] for supporting/controlling commands.


CL:008E.01.51.06.1 - A controlling node MUST NOT associate Node A to a Node B destination if Node B was not
granted Node A’s highest Security Class.


**6.3.7.4.1** **Removing** **associations**


CL:008E.01.51.05.1 A controlling node MUST NOT remove already associated nodes to a destination Group to associate
themselves, unless:


     - The destination NodeID/Endpoint has left the network (i.e. SIS has received a Device Reset
Locally Notification)


     - The destination has changed capabilities and does not support the command received via the
association group (also if a Multi Channel End Point is removed).

     - An end user has actively confirmed to remove associations


     - The lifeline group is full and the controlling node has the SIS Role.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1149




<!-- PAGE 1151 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.8** **Version** **Command** **Class,** **version** **1-3**


**6.3.8.1** **Mandatory** **node** **interview**


CL:0086.01.21.01.2 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.36.


Figure 6.36: Version Command Class interview


CL:0086.01.21.02.1 The interview part starting from the Version Capabilities Get Command is optional. The Controlling node MUST interview the Version Capability Get Command before issuing the Version Z-Wave
Software Get Command if the Controlling node has the intent of using the Z-Wave software version.


**6.3.8.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.3.8.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1150




<!-- PAGE 1152 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.8.4** **Additional** **control** **requirements**


CL:0086.01.51.01.1 A controlling node interviewing a Multi Channel End Point MUST request the End Point’s Command
Class version from the Root Device if the End Point does not advertise support for the Version
Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1151




<!-- PAGE 1153 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.9** **Wake-Up** **Command** **Class,** **version** **1-2**


**6.3.9.1** **Mandatory** **node** **interview**


CL:0084.01.23.01.1 If the controlling node has the inclusion controller or secondary controller role in a network, it MAY

CL:0084.01.21.01.2 skip the node interview. In any case, it MUST NOT issue a Wake-Up Interval Set to a supporting
node.


CL:0084.01.21.02.1 If the controlling node has the SIS or primary controller role in a network, it MUST perform a
supporting node interview according to Figure 6.37.


Figure 6.37: Wake Up Command Class interview


CL:0084.01.21.03.1 A controlling node MUST set a supported Wake Up Interval time value when commissioning a version
2 supporting node.


CL:0084.01.21.04.1 A controlling node MUST set its own NodeID as the Wake-Up destination.


**6.3.9.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.3.9.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


CL:0084.01.42.01.1 A controlling node queuing commands for a Wake-Up node SHOULD indicate to the end user that
the commands will be transmitted when the destination wakes up again.


CL:0084.01.43.01.1 A controlling node MAY show to the end user the expected time until the next Wake-Up.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1152




<!-- PAGE 1154 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.9.4** **Additional** **control** **requirements**


CL:0084.01.52.01.1 A controlling node SHOULD verify that the Wake Up Interval Set Command executed successfully
by either using Supervision encapsulation or reading back the Wake Up Interval settings.


CL:0084.01.52.02.1 If the Wake Up Interval Set Command was ignored by a version 1 supporting node, the controlling
node SHOULD try again using the currently defined interval at the supporting node and its NodeID.


CL:0084.01.52.03.1 A controlling node SHOULD read the Wake Up Interval of a supporting node when the delays between
Wake Up periods are larger than what was last set at the supporting node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1153




<!-- PAGE 1155 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **6.4 Transport Encapsulation Command Class Control Defini-** **tions**


**6.4.1** **CRC-16** **Encapsulation** **Command** **Class** **Control** **Definitions,** **version** **1**


**6.4.1.1** **Mandatory** **node** **interview**


No node interview is required for this Command Class


**6.4.1.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.4.1.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.4.1.4** **Additional** **Control** **Requirements**


CL:0056.01.52.01.1 A controlling node SHOULD use CRC-16 encapsulation to communicate with a supporting node when
no security encapsulation is used and the communication speed is lower than 100 kbits/s.


CL:0056.01.51.01.1 A controlling node MUST support the CRC-16 Command Class and correctly handle received commands encapsulated with CRC-16.


CL:0056.01.51.02.1 A controlling node MUST use CRC-16 encapsulation to return a response to a command if the request
was received using CRC-16 encapsulation (aka “answer-as-asked”).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1154




<!-- PAGE 1156 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.4.2** **Multi** **Channel** **Command** **Class,** **version** **3-4**


**6.4.2.1** **Mandatory** **node** **interview**


CL:0060.01.21.01.3 A node controlling this Command Class MUST perform a supporting node interview as follows:


Figure 6.38: Multi Channel Command Class interview


CL:0060.01.23.01.1 A controlling node MAY skip the interview of aggregated End Points and MAY skip issuing a Multi
Channel Capability Get for any of the aggregated endpoints.


CL:0060.01.23.02.1 A controlling node MAY skip sending a _Multi_ _Channel_ _End_ _Point_ _Find_ _Report_ _Command_ if there are
no dynamic endpoints. ( _Dynamic_ field set to 0 in the _Multi_ _Channel_ _End_ _Point_ _Report_ _Command_ ).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1155




<!-- PAGE 1157 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.4.2.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.4.2.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.4.2.4** **Additional** **Control** **Requirements**


CL:0060.01.51.01.2 A node controlling this Command Class MUST provide control of all its controlled command classes
on every individual End Point.


**6.4.2.4.1** **Root** **Device** **and** **End** **Point** **Command** **Classes**


When End Point functionality is advertised in the Root Device NIF, service discovery mechanisms
like mDNS and installer-style GUIs risk presenting a Root Device functionality which is actually a
mirror representation of an End Point functionality.


Therefore, application command classes of the Root Device capabilities that are also advertised by at

CL:0060.01.52.01.1
least one End Point SHOULD be filtered out by controlling nodes before presenting the functionalities
via service discovery mechanisms like mDNS or to users in a GUI.


**6.4.2.4.2** **S0** **only** **Multi** **Channel** **nodes**


The following considerations apply for nodes supporting S0 and Multi Channel Command Class but
do not support S2 Command Class.


Legacy S0 only nodes may implement some secure and some non-secure End Points. Such a node
supporting S0 must advertise S0 in the Multi Channel Capability Report Command for a given End
point if the End Point can be addressed with S0 encapsulation.


CL:0060.01.52.02.1 A controlling node SHOULD use S0 encapsulation with all End Points if the Root Device was bootstrapped with the S0 Command Class.


CL:0060.01.53.01.1 A controlling node MAY interview and control Command Classes present in the Multi Channel Capability Report of an End Point non-securely if the End Point does not respond to S0 encapsulated
traffic.


**6.4.2.4.3** **Association** **and** **Multi** **Channel** **Association** **mapping**


The following considerations apply for nodes supporting Association and/or Multi Channel Association
and Multi Channel Command Class.


The Association groups functionality may be fully or partially mirrored between the Root Device and
End Points. For example, an Association Remove Command issued to the Root Device may clear the
association destination at the End Point groups.


CL:0060.01.52.03.1 A controlling node SHOULD read back the destinations in every group, including End Points groups
after configuring associations.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1156




<!-- PAGE 1158 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.4.3** **Security** **0** **Command** **Class**


**6.4.3.1** **Mandatory** **node** **interview**


CL:0098.01.21.01.1 A node controlling this Command Class MUST observe the _Role Type Specification_ requirements when
including an S0 node.


**6.4.3.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.4.3.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.4.3.4** **Additional** **Control** **Requirements**


A node is controlling S0 when it can perform S0 bootstrapping of other nodes. The S0 bootstrapping
CL:0098.01.51.01.1 process is described in _Security_ _0_ _(S0)_ _Command_ _Class,_ _version_ _1_ and a controlling node MUST
observe these requirements.


CL:0098.01.51.02.1 A node controlling this Command Class MUST provide control of all its controlled command classes
using S0 encapsulation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1157




<!-- PAGE 1159 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.4.4** **Security** **2** **Command** **Class**


**6.4.4.1** **Mandatory** **node** **interview**


CL:009F.01.21.01.1 A node controlling this command class MUST observe the _Role_ _Type_ _Specification_ requirements when
including an S2 node.


**6.4.4.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.4.4.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.4.4.4** **Additional** **Control** **Requirements**


S2 Security is controlled when a node can perform S2 bootstrapping of other nodes. The Bootstrapping
CL:009F.01.51.01.1 process is described in _Security 2 (S2) Command Class, version 1_ and a controlling node MUST observe
these requirements.


CL:009F.01.51.02.1 A node controlling this Command Class MUST provide control of all its controlled command classes
using S2 encapsulation and at all its granted S2 Security Classes.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1158