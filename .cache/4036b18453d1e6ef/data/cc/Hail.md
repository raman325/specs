<!-- PAGE 706 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.24** **Hail** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **HAS** **BEEN** **OBSOLETED**


New implementations MUST report local state updates via the Lifeline Association Group or use
dedicated Command Classes for application specific purposes. Refer to [34].


The Hail Command Class used by applications to hail other devices in the Z-Wave network. The
usage of the Hail Command Class is application specific.


**3.2.24.1** **Hail** **Command**


Application can send unsolicited Hail Command to other devices in a Z-Wave network.


Table 3.105: Hail Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HAIL|Command Class = COMMAND_CLASS_HAIL|Command Class = COMMAND_CLASS_HAIL|Command Class = COMMAND_CLASS_HAIL|Command Class = COMMAND_CLASS_HAIL|Command Class = COMMAND_CLASS_HAIL|Command Class = COMMAND_CLASS_HAIL|Command Class = COMMAND_CLASS_HAIL|
|Command = HAIL|Command = HAIL|Command = HAIL|Command = HAIL|Command = HAIL|Command = HAIL|Command = HAIL|Command = HAIL|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 705