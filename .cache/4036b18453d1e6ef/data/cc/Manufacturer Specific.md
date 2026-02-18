<!-- PAGE 727 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.30** **Manufacturer** **Specific** **Command** **Class,** **version** **1**


The Manufacturer Specific Command Class is used to advertise manufacturer specific information.
Version 2 of this command class further allows device specific information to be advertised.


**3.2.30.1** **Security** **Considerations**


This Command Class provides information about the device implementation. This information can
potentially be used by an attacker to find vulnerabilities.


CC:0072.01.00.41.004 In order to increase interoperability with legacy controlling nodes, a node supporting the Security 0
Command Class MUST reply to Manufacturer Specific Get Commands received non-securely if it was
granted the S0 network key as its highest Security Class.

CC:0072.01.00.43.001 In this case, it is OPTIONAL for the node to advertise the Manufacturer Specific Command Class in
its NIF.


**3.2.30.2** **Manufacturer** **Specific** **Get** **Command**


This command is used to request manufacturer specific information from another node.

CC:0072.01.04.11.001 The Manufacturer Specific Report Command MUST be returned in response to this command.


CC:0072.01.04.11.002 This command MUST NOT be issued via multicast addressing.


CC:0072.01.04.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.122: Manufacturer Specific Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|
|Command = MANUFACTURER_SPECIFIC_GET|Command = MANUFACTURER_SPECIFIC_GET|Command = MANUFACTURER_SPECIFIC_GET|Command = MANUFACTURER_SPECIFIC_GET|Command = MANUFACTURER_SPECIFIC_GET|Command = MANUFACTURER_SPECIFIC_GET|Command = MANUFACTURER_SPECIFIC_GET|Command = MANUFACTURER_SPECIFIC_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 726




<!-- PAGE 728 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.30.3** **Manufacturer** **Specific** **Report** **Command**


This command is used to advertise manufacturer specific device information.


Table 3.123: Manufacturer Specific Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|
|Command = MANUFACTURER_SPECIFIC_REPORT|Command = MANUFACTURER_SPECIFIC_REPORT|Command = MANUFACTURER_SPECIFIC_REPORT|Command = MANUFACTURER_SPECIFIC_REPORT|Command = MANUFACTURER_SPECIFIC_REPORT|Command = MANUFACTURER_SPECIFIC_REPORT|Command = MANUFACTURER_SPECIFIC_REPORT|Command = MANUFACTURER_SPECIFIC_REPORT|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Product Type ID 1|Product Type ID 1|Product Type ID 1|Product Type ID 1|Product Type ID 1|Product Type ID 1|Product Type ID 1|Product Type ID 1|
|Product Type ID 2|Product Type ID 2|Product Type ID 2|Product Type ID 2|Product Type ID 2|Product Type ID 2|Product Type ID 2|Product Type ID 2|
|Product ID 1|Product ID 1|Product ID 1|Product ID 1|Product ID 1|Product ID 1|Product ID 1|Product ID 1|
|Product ID 2|Product ID 2|Product ID 2|Product ID 2|Product ID 2|Product ID 2|Product ID 2|Product ID 2|



**Manufacturer** **ID** **(16** **bits)**

CC:0072.01.05.11.001 The Manufacturer ID field MUST carry the unique ID identifying the manufacturer of the device.

Manufacturer identifiers can be found in [32]. The first byte is the most significant byte.


**Product** **Type** **ID** **(16** **bits)**

CC:0072.01.05.11.002 The Product Type ID field MUST carry a unique ID identifying the actual product type.

The first byte is the most significant byte.

CC:0072.01.05.11.003 A specific Product Type ID MUST be defined by the manufacturer for each type of product.


**Product** **ID** **(16** **bits)**

CC:0072.01.05.11.004 The Product ID field MUST carry a unique ID identifying the actual product.

The first byte is the most significant byte.

CC:0072.01.05.11.005 A specific Product ID MUST be defined by the manufacturer for each product of a given product
type. Thus, the same Product ID value may appear for different Product Type ID values.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 727

---

<!-- PAGE 729 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.31** **Manufacturer** **Specific** **Command** **Class,** **version** **2**


Manufacturer Specific Command Class, version 2 adds a set of commands to communicate unique
identification, e.g. the serial number, of the product.

Commands not mentioned here remains unchanged as specified for Manufacturer Specific Command
Class, Version 1.


**3.2.31.1** **Security** **Considerations**


A supporting node MUST comply with Section 3.2.30.1 Security Considerations


**3.2.31.2** **Device** **Specific** **Get** **Command**


This command is used to request device specific information.

CC:0072.02.06.11.001 The Device Specific Report Command MUST be returned in response to this command.


CC:0072.02.06.11.002 This command MUST NOT be issued via multicast addressing.


CC:0072.02.06.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.124: Device Specific Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|
|Command = DEVICE_SPECIFIC_GET|Command = DEVICE_SPECIFIC_GET|Command = DEVICE_SPECIFIC_GET|Command = DEVICE_SPECIFIC_GET|Command = DEVICE_SPECIFIC_GET|Command = DEVICE_SPECIFIC_GET|Command = DEVICE_SPECIFIC_GET|Command = DEVICE_SPECIFIC_GET|
|Reserved|Reserved|Reserved|Reserved|Reserved|Device ID Type|Device ID Type|Device ID Type|



**Device** **ID** **Type** **(3** **bits)**

This field contains values for the Device ID Type.


CC:0072.02.06.12.001

|Table 3.125: Device ID Type (3 bits) Device ID Type|Value|
|---|---|
|Device ID Type|Value|
|Return OEM factory default Device ID Type|0|
|Serial Number|1|
|Pseudo Random|2|
|Reserved|3-7|

A sending node SHOULD specify a value of zero when issuing the Device Specific Get command since
the responding node may only be able to return one Device ID Type.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 728




<!-- PAGE 730 -->

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|Command Class = COMMAND_CLASS_MANUFACTURER_SPECIFIC|
|Command = DEVICE_SPECIFIC_REPORT|Command = DEVICE_SPECIFIC_REPORT|Command = DEVICE_SPECIFIC_REPORT|Command = DEVICE_SPECIFIC_REPORT|Command = DEVICE_SPECIFIC_REPORT|Command = DEVICE_SPECIFIC_REPORT|Command = DEVICE_SPECIFIC_REPORT|Command = DEVICE_SPECIFIC_REPORT|
|Reserved|Reserved|Reserved|Reserved|Reserved|Device ID Type|Device ID Type|Device ID Type|
|Device ID Format|Device ID Format|Device ID Format|Device ID Length|Device ID Length|Device ID Length|Device ID Length|Device ID Length|
|Device ID Data 1|Device ID Data 1|Device ID Data 1|Device ID Data 1|Device ID Data 1|Device ID Data 1|Device ID Data 1|Device ID Data 1|
|…|…|…|…|…|…|…|…|
|Device ID Data N|Device ID Data N|Device ID Data N|Device ID Data N|Device ID Data N|Device ID Data N|Device ID Data N|Device ID Data N|



CC:0072.02.07.11.001


CC:0072.02.07.11.002



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.31.3** **Device** **Specific** **Report** **Command**


This command is used to advertise device specific information.


Table 3.126: Device Specific Report Command


**Device** **ID** **Data** **Format** **(3** **bits)**

This command field defines the format used for Device ID Data.


Table 3.127: Device ID Data Format (3 bits)


|Device ID Data Format|Value|Description|
|---|---|---|
|UTF-8|0x00|The Device ID Data MUST be in UTF-8<br>format.|
|Binary|0x01|The Device ID Data is in plain binary<br>format and MUST be displayed as hex-<br>adecimal values e.g.<br>0x30, 0x31, 0x32,<br>0x33 MUST be displayed as h’30313233.|



CC:0072.02.07.11.003 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Device** **ID** **Type** **(3** **bits)**

This field contains values for the Device ID Type. See Device Specific Get Command for details.

In case the Device ID Type specified in a Device Specific Get command is not supported by the

CC:0072.02.07.13.001
responding node, the responding node MAY return the factory default Device ID Type (as if receiving
the value 0 in the Device Specific Get command).


**Device** **ID** **Data** **Length** **(5** **bits)**


CC:0072.02.07.11.004
This field contains the length of the Device ID Data field. The field MUST NOT carry the value zero.


**Device** **ID** **Data** **(N** **bytes)**

Data fields for Device ID. “Device ID Data Format” defines data format and “Device ID Data Length
Indicator” defines length.


CC:0072.02.07.11.005 The Manufacturer ID and Device ID combination MUST be globally unique.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 729