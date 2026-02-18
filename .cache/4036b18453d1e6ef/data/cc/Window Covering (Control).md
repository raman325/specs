<!-- PAGE 1138 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.22** **Window** **Covering** **Command** **Class,** **version** **1**


**6.2.22.1** **Mandatory** **interview**


CL:006A.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.28.


Figure 6.28: Window Covering Command Class interview


**6.2.22.2** **Minimum** **end** **user** **functionalities**


CL:006A.01.31.02.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.22.2.1** **Go** **to** **position**


CL:006A.01.31.02.1 This action MUST be available to the end user for parameters ID with known positions (odd parameters IDs). When the end user performs this action, the issued command MUST comply with Table
6.38.

|Field|Table 6.38: Window Covering::Go to a Position Value|
|---|---|
|Field|Value|
|Command|WINDOW_COVERING_SET<br>|
|Parameter count|User defned ( 0x01)<br>|
|Parameter ID x|User defned among supported (odd values)<br>|
|Value x|User defned among 0x00..0x63<br>|
|Duration|User defned or 0xFF|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1137




<!-- PAGE 1139 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.22.2.2** **Start** **level** **change** **up** **or** **down**


CL:006A.01.31.03.1 This action MUST be available to the end user for all supported parameters ID. When the end user
performs this action, the issued command MUST comply with Table 6.39.


Table 6.39: Window Covering::Start Level Change Up or Down

|Field|Value|
|---|---|
|Command|WINDOW_COVERING_START_LEVEL_CHANGE<br>|
|Up/Down|User defned among 0x00 and 0x01<br>|
|Parameter ID|User defned among supported parameters ID<br>|
|Duration|User defned or 0xFF|



**6.2.22.2.3** **Stop** **level** **change**


CL:006A.01.31.04.1 This action MUST be available to the end user for all supported parameters ID. When the end user
performs this action, the issued command MUST comply with Table 6.40.

|Field|Table 6.40: Window Covering::Stop Level Change Value|
|---|---|
|Field|Value|
|Command|WINDOW_COVERING_STOP_LEVEL_CHANGE<br>|
|Parameter ID|User defned among supported parameters ID|



**6.2.22.3** **Node** **properties**


CL:006A.01.42.01.1 Controller SHOULD have a UI allowing the end user to see the following properties:


     - Last known position/value for all parameters IDs with known position


**6.2.22.4** **Additional** **control** **requirements**


CL:006A.01.51.01.2 A controlling node MUST NOT interview and provide controlling functionalities for the Multilevel
Switch Command Class for a node (or endpoint) supporting this Command Class, as it is a fully
redundant and less precise application functionality.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1138




<!-- PAGE 1140 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **6.3 Management Command Class Control Definitions**


**6.3.1** **Association** **Command** **Class,** **version** **1-4**


**6.3.1.1** **Mandatory** **Node** **interview**


CL:0085.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.29.


Figure 6.29: Association Command Class interview


**6.3.1.2** **Minimum** **End** **User** **functionalities**


No minimum end user functionality is required for this Command Class.


A controlling node implementing a UI that allows an end user to establish association between nodes
CL:0085.01.31.01.1 MUST NOT restrict the end user from establishing associations that are allowed. Refer to Section
6.3.1.4 for allowed associations.


**6.3.1.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.3.1.4** **Additional** **Control** **requirements**


If the supporting node also supports Multi Channel Association and the controlling node controls
CL:0085.01.51.01.1 Multi Channel Association, the controlling node MUST interview and control the Multi Channel
Association Command Class instead of this Command Class.


CL:0085.01.51.02.1 A controlling node MUST use the Association Group Information (AGI) Command Class to probe the
commands that a given association group will be sending before creating associations towards other
nodes.


If an association group in a Node A sends one or more controlling commands:


CL:0085.01.51.03.3


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1139




<!-- PAGE 1141 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


     - A controlling node MUST NOT associate Node A to a Node B destination that does not support
the Command Class that the Node A will be controlling.


CL:0085.01.53.01.3 - A controlling node MAY create an association to a destination supporting an actuator Command
Class if the actual association group sends Basic Control Command Class.


For Association version 1 and version 2:


CL:0085.01.51.04.3 **–** A controlling node MUST NOT associate Node A to a Node B destination if Node A and
Node B’s highest Security Class are not identical.


For Association version 3 or newer:


CL:0085.03.51.01.1 **–** A controlling node MUST NOT associate Node A to a Node B destination if Node A was
not granted Node B’s highest Security Class.


If an association group in Node A sends only supporting commands:


CL:0085.01.53.02.3 - A controlling node MAY create an association to any Node B destination if the actual association
group sends commands reflecting the support of a Command Class by the sending Node/End
Point. Refer to [25] for supporting/controlling commands.


CL:0085.01.51.06.1 - A controlling node MUST NOT associate Node A to a Node B destination if Node B was not
granted Node A’s highest Security Class.


**6.3.1.4.1** **Removing** **associations**


CL:0085.01.51.05.1 A controlling node MUST NOT remove already associated nodes to a destination Group to associate
themselves, unless:


     - The destination NodeID/Endpoint has left the network (i.e. SIS has received a Device Reset
Locally Notification)


     - The destination of a group has changed capabilities and does not support the command received
via the association group (also if a Multi Channel End Point is removed).

     - An end user has actively confirmed to remove associations


     - The lifeline group is full and the controlling node has the SIS Role.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1140




<!-- PAGE 1142 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.2** **Association** **Group** **Information** **(AGI)** **Command** **Class,** **version** **1-3**


**6.3.2.1** **Mandatory** **node** **interview**


CL:0059.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.30.


Figure 6.30: Association Group Information (AGI) Command Class interview


CL:0059.01.23.01.1 A controlling node MAY issue a single Association Group Info Get Command by using the List Mode
flag.


**6.3.2.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.3.2.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1141