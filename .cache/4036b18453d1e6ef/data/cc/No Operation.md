<!-- PAGE 1018 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.6** **No** **Operation** **Command** **Class,** **version** **1**


The No Operation Command Class is used to check if a node is reachable by sending a Command
less frame to the specified destination. Feature used by the Z-Wave protocol in many situations e.g.
checking that an excluded node is non-responding. This Command can also be used on application
level e.g. checking if a SUC/SIS is reachable from a new node in the network. This command class
contains no command identifier and data.


**Notice** : It is not necessary to announce the No Operation Command Class in the NIF.


Table 5.133: No Operation Command Class, version 1

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1017