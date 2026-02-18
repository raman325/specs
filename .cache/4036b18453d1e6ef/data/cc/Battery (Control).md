<!-- PAGE 1143 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.3** **Battery** **Command** **Class,** **version** **1**


**6.3.3.1** **Mandatory** **node** **interview**


CL:0080:01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.31


Figure 6.31: Battery Command Class interview


**6.3.3.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.3.3.3** **Node** **properties**


CL:0080.01.41.01.1 A controlling node MUST allow the end user to see the last known battery level.


**6.3.3.4** **Additional** **control** **requirements**


CL:0080.01.52.01.1 Unless unsolicited Battery Report Commands are received, a controlling node SHOULD Probe the
current battery level at least every month


CL:0080.01.51.02.1 A controlling node MUST indicate to the end user that the battery needs to be replaced or reloaded
when the supporting node issues a Battery Report with the _Battery_ _Level_ field set to 0xFF.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1142