<!-- PAGE 281 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.54** **Manufacturer** **Proprietary** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **OBSOLETED**


New implementations MUST NOT support this Command Class. Consult the Z-Wave Alliance
when your application does not seem to fit any existing Command Class.


The Manufacturer Proprietary Command Class is used to transfer data between devices in the Z-Wave
network. The data content MUST be vendor specific and MUST be non-value added with respect
to the Home Automation application in general. An example could be data used to diagnose the
hardware in a device.


**Note** : Do not use the Manufacturer Proprietary Command Class without written approval from the
Z-Wave Alliance.


**2.2.54.1** **Manufacturer** **Proprietary** **Command**


This command is used to transfer proprietary commands between devices. The Command features
a manufacturer specific identifier to allow the receiving device to check if this Command can be
interpreted. The vendor is responsible for establishing a Command structure to differ between the set
of Commands supported.


In order not to congest the Z-Wave network, large data transfers MUST leave transmit opportunities
for other nodes in the network. If sending a command longer than two frames, a node MUST implement
a delay between every transmitted frame. The minimum required time delay and number of frames
before a delay must be inserted depends on the actual bit rate.


 - 40 kbit/s: At least 35 ms if sending more than 2 frames back-to-back


 - 100 kbit/s: At least 15 ms if sending more than 2 frames back-to-back


Table 2.337: Manufacturer Proprietary Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MANUFACTURER_PROPRIETARY|Command Class = COMMAND_CLASS_MANUFACTURER_PROPRIETARY|Command Class = COMMAND_CLASS_MANUFACTURER_PROPRIETARY|Command Class = COMMAND_CLASS_MANUFACTURER_PROPRIETARY|Command Class = COMMAND_CLASS_MANUFACTURER_PROPRIETARY|Command Class = COMMAND_CLASS_MANUFACTURER_PROPRIETARY|Command Class = COMMAND_CLASS_MANUFACTURER_PROPRIETARY|Command Class = COMMAND_CLASS_MANUFACTURER_PROPRIETARY|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|
|…|…|…|…|…|…|…|…|
|Data N|Data N|Data N|Data N|Data N|Data N|Data N|Data N|



**Manufacturer** **ID** **(16** **bits)**


The Manufacturer ID is a unique ID identifying the manufacturer of the device. Manufacturer identifiers can be found in [32].

The first byte (Manufacturer ID 1) is the most significant byte.


**Data** **(N** **bytes)**

The data fields may be used for data transfer etc. The number of data fields transmitted MUST be
determined from the length field in the frame.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 280