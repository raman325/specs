<!-- PAGE 369 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.77** **Proprietary** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **OBSOLETED**


New implementations MUST NOT support this Command Class. Consult the Z-Wave Alliance
when your application does not seem to fit any existing Command Class.


The Proprietary Command Class is used to transfer data between devices. The data content MUST
be vendor specific and commands MUST NOT provide any value-add with respect to the Home
Automation application in general.


**2.2.77.1** **Proprietary** **set** **command**


This command is used to transfer data to a device.


Table 2.447: Proprietary Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|
|Command = PROPRIETARY_SET|Command = PROPRIETARY_SET|Command = PROPRIETARY_SET|Command = PROPRIETARY_SET|Command = PROPRIETARY_SET|Command = PROPRIETARY_SET|Command = PROPRIETARY_SET|Command = PROPRIETARY_SET|
|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|
|…|…|…|…|…|…|…|…|
|Data N|Data N|Data N|Data N|Data N|Data N|Data N|Data N|



**Data** **(N** **bytes)**

The data fields may be used to set various data in the device. The number of data fields transmitted
MUST be determined from the length field in the frame.


**2.2.77.2** **Proprietary** **get** **command**


This command is used to request data from a device.


The Proprietary Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.448: Proprietary Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|
|Command = PROPRIETARY_GET|Command = PROPRIETARY_GET|Command = PROPRIETARY_GET|Command = PROPRIETARY_GET|Command = PROPRIETARY_GET|Command = PROPRIETARY_GET|Command = PROPRIETARY_GET|Command = PROPRIETARY_GET|
|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|
|…|…|…|…|…|…|…|…|
|Data N|Data N|Data N|Data N|Data N|Data N|Data N|Data N|



**Data** **(N** **bytes)**


Refer to explanation under the Proprietary Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 368




<!-- PAGE 370 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.77.3** **Proprietary** **report** **command**


This command is used to retrieve various data from a device.


Table 2.449: Proprietary Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|Command Class = COMMAND_CLASS_PROPRIETARY|
|Command = PROPRIETARY_REPORT|Command = PROPRIETARY_REPORT|Command = PROPRIETARY_REPORT|Command = PROPRIETARY_REPORT|Command = PROPRIETARY_REPORT|Command = PROPRIETARY_REPORT|Command = PROPRIETARY_REPORT|Command = PROPRIETARY_REPORT|
|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|
|…|…|…|…|…|…|…|…|
|Data N|Data N|Data N|Data N|Data N|Data N|Data N|Data N|



**Data** **(N** **bytes)**


Refer to explanation under the Proprietary Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 369