<!-- PAGE 1104 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.9** **Entry** **Control** **Command** **Class,** **version** **1**


**6.2.9.1** **Mandatory** **node** **interview**


CL:006F.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.9.


Figure 6.9: Entry Control Command Class interview


CL:006F.01.23.01.1 A node controlling this command class MAY skip the AGI Interview (refer to Section 6.3.2) if the
supporting node is a Z-Wave Plus node and the controlling node has estalished a Lifeline Association.


**6.2.9.2** **Minimum** **end** **user** **functionalities**


CL:006F.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.9.2.1** **Configure** **the** **keypad**


CL:006F.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.14.


Table 6.14: Entry Control Keypad::Configure the keypad

|Field|Value|
|---|---|
|Command|ENTRY_CONTROL_CONFIGURATION_SET<br>|
|Key Cache Size|User defned among supported values<br>|
|Key Cache Timeout|User defned among supported values|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1103




<!-- PAGE 1105 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.9.3** **Node** **properties**


CL:006F.01.41.01.1 A controlling node MUST have a UI allowing the end user to see the received Entry Control Notifications (Event type and data)


**6.2.9.4** **Additional** **control** **requirements**


CL:006F.01.51.01.1 A node controlling this command class MUST also control:


     - Association Command Class, version 2


     - Association Group Information, version 3

CL:006F.01.51.02.1 A controlling node MUST associate itself to a group issuing Entry Control Notification Commands
before performing a supporting node interview and providing end user functionalities.


CL:006F.01.51.03.1 A controlling node MUST NOT remove associations in order to associate itself to an association group
issuing Entry Control Notification Commands.


CL:006F.01.52.01.1 A controlling node SHOULD NOT provide end user functionalities if it cannot associate itself to
an association group sending Entry Control Notification Commands. (e.g. all Association Groups
sending the relevant command are full)

CL:006F.01.52.02.1 A controlling node SHOULD have a UI allowing the end user to define what actions to take based on
received Entry Control Notifications.


CL:006F.01.52.03.1 A controlling node SHOULD also control Door Lock Command Class and Barrier Operator Command
Class. It SHOULD also allow the user to set the door mode or initiate opening/closing of a given
node based on received Entry Control Notifications.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1104