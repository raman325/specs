<!-- PAGE 1089 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **6.2 Application Command Class Control Definitions**


**6.2.1** **Anti-theft** **Unlock** **Command** **Class,** **version** **1**


**6.2.1.1** **Mandatory** **node** **interview**


CL:007E.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.4.


Figure 6.1: Anti-Theft Unlock Command Class interview


**6.2.1.2** **Minimum** **end** **user** **functionalities**


**6.2.1.2.1** **Unlock** **the** **node**


CL:007E.01.31.01.1 If the supporting node is in the locked state and runs in restricted mode, the end user MUST be

CL:007E.01.31.01.1 able send an unlock command. When the end user performs this action, the issued command MUST
comply with Table 6.1.



CL:007E.01.32.01.1



|Field|Table 6.1: Anti-Theft Unlock::Unlock the node Value|
|---|---|
|Field|Value|
|Command|COMMAND_ANTITHEFT_UNLOCK_SET<br>|
|Magic Code length|Controlling node defned in 0x01..0xA, based on user input.<br>|
|Magic Code|User defned<br>The Magic Code SHOULD be shown as a hexadecimal value to the end<br>users.|


**6.2.1.3** **Node** **properties**



CL:007E.01.41.01.1 If the supporting node is in the locked state and runs in restricted mode, the controlling node MUST
have a UI allowing the end user to see that the supporting node is restricted and that the supporting
node requires unlocking to use the full functionality.


CL:007E.01.43.01.1 A controlling node MAY display the information provided in [25] for the reported Z-Wave Alliance
locking entity ID.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1088