<!-- PAGE 1090 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.2** **Barrier** **Operator** **Command** **Class,** **version** **1**


**6.2.2.1** **Mandatory** **node** **interview**


CL:0066.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.2.


Figure 6.2: Barrier Operator Command Class interview


**6.2.2.2** **Minimum** **end** **user** **functionalities**


CL:0066.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.2.2.1** **Initiate** **opening** **(or** **stop** **closing)**


CL:0066.01.31.03.1 When the end user performs this action, the issued command MUST comply with Table 6.2.

|Table Field|6.2: Barrier Operator::Initiate opening (or stop closing) Value|
|---|---|
|Field|Value|
|Command|BARRIER_OPERATOR_SET|
|Target Value|0xFF|



**6.2.2.2.2** **Initiate** **closing**


CL:0066.01.31.04.1 When the end user performs this action, the issued command MUST comply with Table 6.3.


Table 6.3: Barrier Operator::Initiate closing

|Field|Value|
|---|---|
|Command|BARRIER_OPERATOR_SET|
|Target Value|0x00|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1089




<!-- PAGE 1091 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.2.3** **Node** **properties**


CL:0066.01.42.01.1 The controlling node SHOULD have a UI allowing the end user to see/access the following properties:


     - Last known Barrier State (Open, Closed, stopped at a % position or unknown)


     - Last known Subsystems’ state (ON/OFF), if any


**6.2.2.4** **Additional** **control** **requirements**


CL:0066.01.52.01.2 A node controlling this command class SHOULD also control the Notification Command Class. A
node controlling this command class SHOULD activate all supported subsystems by default.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1090




<!-- PAGE 1092 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.3** **Basic** **Command** **Class,** **version** **1-2**


**6.2.3.1** **Mandatory** **node** **interview**


CL:0020.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.3.


Figure 6.3: Basic Command Class interview


CL:0020.01.21.02.2 A controlling node MUST conclude that the Basic Command Class is not supported by a node (or
endpoint) if no Basic Report is returned.


**6.2.3.2** **Minimum** **end** **user** **functionalities**


CL:0020.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.3.2.1** **Set** **the** **node** **On/Off** **state**


CL:0020.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.4

|Field|Table 6.4: Basic::Set the node state Value|
|---|---|
|Field|Value|
|Command|BASIC_SET<br>|
|Value|User defned among 0x00 and 0xFF.<br>More values MAY be available to the end user.|



**6.2.3.3** **Node** **properties**


CL:0020.01.43.01.1 A controlling node MAY have a UI allowing the end user to see the following properties:

     - Last known state (On or Off)

CL:0020.01.42.01.1 A controlling node SHOULD NOT assume that the last state is as defined in the last Set Command
and SHOULD issue a subsequent Basic Get Command even if receiving a Supervision SUCCESS
status after issuing a Basic Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1091




<!-- PAGE 1093 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.3.4** **Additional** **control** **requirements**


CL:0020.01.51.01.3 A controlling node MUST NOT use the Basic Command Class for controlling nor showing status (receiving report) of a node (or endpoint) if the controlling node controls at least one actuator command
class supported by a node (or endpoint). The actuator command classes are defined in _Application_
_Command_ _Classes_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1092




<!-- PAGE 1094 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.4** **Binary** **Switch** **Command** **Class,** **version** **1-2**


**6.2.4.1** **Mandatory** **node** **interview**


CL:0025.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.4.


Figure 6.4: Binary Switch Command Class Interview


**6.2.4.2** **Minimum** **end** **user** **functionalities**


CL:0025.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.4.2.1** **Set** **the** **node** **On/Off** **state**


CL:0025.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.5.

|Field|Table 6.5: Binary Switch::Set the node state Value|
|---|---|
|**Field**|**Value**|
|Command|SWITCH_BINARY_SET<br>|
|Value|User defned among 0x00 and 0xFF.<br>|
|Duration (v2)|User defned or 0xFF|



**6.2.4.3** **Node** **properties**


CL:0025.01.51.01.1 A node controlling this Command Class SHOULD have a UI allowing the end user to see the following
properties:

     - Last known state (On or Off)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1093




<!-- PAGE 1095 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.5** **Central** **Scene** **Command** **Class,** **version** **1-3**


**6.2.5.1** **Mandatory** **node** **interview**


CL:005B.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.5.


Figure 6.5: Central Scene Command Class interview


CL:005B.01.23.01.1 A node controlling this command class MAY skip the AGI Interview (refer to Section 6.3.2) if the
supporting node is a Z-Wave Plus node and the controlling node has estalished a Lifeline Association.


**6.2.5.2** **Minimum** **end** **user** **functionalities**


There is no minimum end user functionalities associated with the control of this Command Class.

CL:005B.01.32.01.1 A controlling node SHOULD allow the user to define which other nodes to actuate when receiving a
Central Scene Notification from a given node with a given key attribute and SceneID.


**6.2.5.3** **Node** **properties**


CL:005B.01.41.01.1 The controlling node MUST have a UI allowing the end user to see how many Scenes ID (or buttons)
and key attributes are supported by a node.

CL:005B.01.41.02.1 The controlling node MUST make received Central Scene Notifications available to the end user.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1094




<!-- PAGE 1096 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.5.4** **Additional** **control** **requirements**


CL:005B.01.51.01.1 A node controlling this command class MUST also control:


     - Association Command Class, version 2


     - Association Group Information, version 3

CL:005B.01.51.02.1 A controlling node MUST associate itself to a group issuing Central Scene Notification Commands in
order to provide end user functionalities.


CL:005B.01.51.03.1 A controlling node MUST NOT remove associations in order to associate itself to an association group
issuing Central Scene Notification Commands.


CL:005B.01.53.01.1 It is OPTIONAL for a controlling node to provide end user functionalities and node properties if it
cannot associate itself to an association group sending Central Scene Notification Commands. (e.g.
all Association Groups sending the relevant command are full)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1095




<!-- PAGE 1097 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.6** **Color** **Switch** **Command** **Class,** **version** **1-3**


**6.2.6.1** **Mandatory** **node** **interview**


CL:0033.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.


Figure 6.6: Color Switch Command Class interview


**6.2.6.2** **Minimum** **end** **user** **functionalities**


CL:0033.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.6.2.1** **Set** **the** **color**


CL:0033.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.6.

|Field|Table 6.6: Color Switch::Set the color Value|
|---|---|
|Field|Value|
|Command|SWITCH_COLOR_SET|
|Color component count|Determined by the controlling node based on user input<br>|
|Color Component ID x|User defned among supported<br>|
|Value x|User defned<br>|
|Duration (v2)|User defned or 0xFF|



CL:0033.01.31.03.1 For this functionality, the color selected by the end user MUST be set using a single command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1096




<!-- PAGE 1098 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.6.2.2** **Fade/enhance** **a** **color** **component**


CL:0033.01.31.04.1 When the end user performs this action, the issued command MUST comply with Table 6.7.


Table 6.7: Color Switch::Fade/enhance a color component

|Field|Value|
|---|---|
|Command|SWITCH_COLOR_START_LEVEL_CHANGE<br>|
|Up/down|User defned<br>|
|Color component ID|User defned among supported<br>|
|Duration (v3)|User defned or 0xFF|



**6.2.6.2.3** **Stop** **fading/enhancing** **a** **color** **component**


CL:0033.01.31.05.1 When the end user performs this action, the issued command MUST comply with Table 6.8.


Table 6.8: Color Switch::Stop fading/enhancing a color component

|Field|Value|
|---|---|
|Command|SWITCH_COLOR_STOP_LEVEL_CHANGE<br>|
|Color component ID|User defned among supported|



**6.2.6.3** **Node** **properties**


CL:0033.01.42.01.1 A controlling node SHOULD have a UI allowing the end user to see the following properties:

     - Last known configured color or color components values


**6.2.6.4** **Additional** **control** **requirements**


CL:0033.01.51.01.1 A node controlling this Command Class MUST also control:


     - Binary Switch Command Class, version 2


     - Multilevel Switch, version 4


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1097




<!-- PAGE 1099 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.7** **Configuration** **Command** **Class,** **version** **1-4**


**6.2.7.1** **Mandatory** **node** **interview**


CL:0070.03.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.7.


Figure 6.7: Configuration Command Class interview


**6.2.7.2** **Minimum** **end** **user** **functionalities**


CL:0070.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.7.2.1** **Set** **a** **configuration** **parameter** **Value**


CL:0070.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.9 for
parameters numbers smaller than 256 and Table 6.10 for parameter numbers greater or equal to 256.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1098




<!-- PAGE 1100 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 6.9: Configuration::Set a (normal) configuration parameter

|Table 6.9: Co value Field|onfiguration::Set a (normal) configuration parameter Value|
|---|---|
|Field|Value|
|Command|CONFIGURATION_SET<br>|
|Parameter number|For version 2 or older: User defned<br>For version 3 or newer: User defned among supported parameter<br>numbers.<br>|
|Size|For version 2 or older: User defned among 1, 2 and 4.<br>For version 3 or newer: Automatically determined from confguration<br>parameter number properties<br>|
|Default|User defned or 0x00<br>For version 3 or older: this feld SHOULD NOT be set to 1.<br>|
|Command|For version 2 or older: User defned.<br>For version 3 or newer: User defned among supported values|



Table 6.10: Configuration::Set an extended range configuration parameter value

|Field|Value|
|---|---|
|Command (v2)<br>|CONFIGURATION_BULK_SET<br>|
|Parameter ofset (v2)|For version 2: User defned among any value (256..65535).<br>For version 3 or newer: User defned among supported parameter<br>numbers.<br>|
|Number of Parameters(v2)|User defned or 0x01.<br>|
|Size (v2)|For version 2: User defned among 1, 2 and 4.<br>For version 3 or newer: Automatically determined from confguration<br>parameter number properties<br>|
|Default (v2)|User defned or 0x00<br>For version 3 or older: this feld SHOULD NOT be set to 1.|
|Handshake (v2)<br>|0x00<br>|
|Confguration Value (v2)|For version 2: User defned.<br>For version 3 or newer: User defned among supported values|



**6.2.7.2.2** **Reset** **all** **configuration** **parameter** **values** **to** **default**


CL:0070.04.31.01.1 When the end user performs this action, the issued command MUST comply with Table 6.11.


Table 6.11: Configuration::Reset all configuration parameter values

|Table 6.11: C to default Field|Configuration::Reset all configuration parameter values Value|
|---|---|
|Field|Value|
|Command (v4)|CONFIGURATION_DEFAULT_RESET|



**6.2.7.3** **Node** **properties**


CL:0070.03.41.01.1 If nodes are version 3, the controlling node MUST have a UI allowing the end user to see supported
parameter numbers, their current value, their allowed value range and their default value.

Values MUST be presented according to the Format advertised in the Configuration Properties Report
Command.


CL:0070.01.41.01.1 If nodes are version 1 or 2, the controlling node MUST have a UI showing the known parameters that
have been set by the end user and their current value.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1099




<!-- PAGE 1101 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.7.4** **Additional** **control** **requirements**


CL:0070.04.51.01.1 If nodes are version 4, a node controlling this command class MUST NOT issue a Bulk Set Command
supporting nodes advertising “No Bulk support” in the Configuration Properties Report Commands.


CL:0070.04.51.02.1 If nodes are version 4, a node controlling this command class MUST NOT allow an end user to
issue a Configuration Set or a Bulk Set Command for parameters advertised as “read-only” in the
Configuration Properties Report Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1100




<!-- PAGE 1102 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.8** **Door** **Lock** **Command** **Class,** **version** **1-4**


**6.2.8.1** **Mandatory** **node** **interview**


CL:0062.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.8.


Figure 6.8: Door Lock Command Class interview


**6.2.8.2** **Minimum** **end** **user** **functionalities**


CL:0062.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.8.2.1** **Configure** **the** **door** **lock**


CL:0062.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.12.


Table 6.12: Door Lock::Configure the door lock

|Field|Value|
|---|---|
|Command|DOOR_LOCK_CONFIGURATION_SET<br>|
|Operation type|For version 4 or newer: User defned among supported operation<br>types.<br>For version 3 or older: User defned among 0x01..0x02|
|Outside Door Handles Mode|Free (0xF recommended)|
|Inside Door Handles Mode|Free (0xF recommended)<br>|
|Lock Timeout Minutes|User defned (0x00..0xFD) if Operation Type is set to 0x02, else<br>0xFE<br>|
|Lock Timeout seconds|User defned (0x00..0x3B) if Operation Type is set to 0x02, else<br>0xFE<br>|
|Auto-relock time (v4)|User defned if supported, else 0<br>|
|Hold and release time (v4)|User defned if supported, else 0<br>|
|BTB (v4)|User defned if supported, else 0<br>|
|TA (v4)|User defned if supported, else 0|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1101




<!-- PAGE 1103 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.8.2.2** **Set** **the** **door** **mode**


CL:0062.01.31.03.1 When the end user performs this action, the issued command MUST comply with Table 6.13.

|Field|Table 6.13: Door Lock::Set the door mode Value|
|---|---|
|Field|Value|
|Command|DOOR_LOCK_CONFIGURATION_SET<br>|
|Door Lock Mode|For version 4 or newer: User defned among supported modes.<br>For version 3 or older: User defned among 0x00 and 0xFF.<br>Timed Operation modes MUST NOT be selectable by the end user if the<br>door lock is not confgured in Timed Operation|



**6.2.8.3** **Node** **properties**


CL:0062.01.41.01.1 Controller SHOULD have a UI allowing the end user to see the following properties:


     - Last known Door Lock mode (Secure, Unsecured, etc.)

     - Current door lock configuration


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1102