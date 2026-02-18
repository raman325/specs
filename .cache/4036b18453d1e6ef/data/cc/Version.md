<!-- PAGE 777 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.43** **Version** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **OBSOLETED**


New implementations MUST NOT support this Command Class.


New implemenetations MUST use the _Version_ _Command_ _Class,_ _version_ _2_, or newer instead.


The Version Command Class may be used to obtain the Z-Wave library type, the Z-Wave protocol
version used by the application, the individual Command Class versions used by the application and
the vendor specific application version from a Z-Wave enabled device.


**3.2.43.1** **Compatibility** **Considerations**


CC:0086.01.00.21.001 In a Multi Channel device, the Version Command Class MUST be supported by the Root Device,

CC:0086.01.00.22.001 while the Version Command Class SHOULD NOT be supported by individual End Points.


There may be cases where a given Command Class is not implemented by the Root Device of a Multi
CC:0086.01.00.21.002 Channel device. However, the Root Device MUST respond to Version requests for any Command
Class implemented by the Multi Channel device; also in cases where the actual Command Class is
only provided by an End Point.


A node supporting a Command Class having a version higher than 1 must support the Version
Command Class to be able to identify the supported version. If a node does not support the _Version_
_Command_ _Class,_ _version_ _1_ _[OBSOLETED]_ at its highest security level, it may be assumed that all
command classes implement version 1.


**3.2.43.2** **Security** **Considerations**


The Version Command Class provides information about the device implementation. This information
can potentially be used by an attacker to find vulnerabilities.


CC:0086.01.00.41.002 If a node supports this Command Class and does not support the Security 2 Command Class, it
MUST comply with Table 3.159.










|Col1|Table 3.159: Version After Non-Secure Inclusion|Command Class Support After Secure Inclusion|
|---|---|---|
||After Non-Secure Inclusion|After Secure Inclusion|
|Non-Secure or<br>Less- Secure<br>communication|The node MUST support<br>the Version Command<br>Class and advertise it in<br>the NIF.|The node MUST NOT support the Version<br>Command Class and MUST NOT advertise it in<br>the NIF or Security Commands Supported<br>Report commands.|
|Secure<br>communication<br>at the highest<br>security class|N/A|The node MUST support the Version Command<br>Class and advertise it in the Security Commands<br>Supported Report commands.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 776




<!-- PAGE 778 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.43.3** **Version** **Get** **Command**


The Version Get Command is used to request the library type, protocol version and application version
from a device that supports the Version Command Class.


CC:0086.01.11.11.001 The Version Report Command MUST be returned in response to this command.


CC:0086.01.11.11.002 This command MUST NOT be issued via multicast addressing.


CC:0086.01.11.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.160: Version Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|
|Command = VERSION_GET|Command = VERSION_GET|Command = VERSION_GET|Command = VERSION_GET|Command = VERSION_GET|Command = VERSION_GET|Command = VERSION_GET|Command = VERSION_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 777




<!-- PAGE 779 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.43.4** **Version** **Report** **Command**


The Version Report Command is be used to advertise the library type, protocol version and application
version from a device.


Table 3.161: Version Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|
|Command = VERSION_REPORT|Command = VERSION_REPORT|Command = VERSION_REPORT|Command = VERSION_REPORT|Command = VERSION_REPORT|Command = VERSION_REPORT|Command = VERSION_REPORT|Command = VERSION_REPORT|
|Z-Wave Library Type|Z-Wave Library Type|Z-Wave Library Type|Z-Wave Library Type|Z-Wave Library Type|Z-Wave Library Type|Z-Wave Library Type|Z-Wave Library Type|
|Z-Wave Protocol Version|Z-Wave Protocol Version|Z-Wave Protocol Version|Z-Wave Protocol Version|Z-Wave Protocol Version|Z-Wave Protocol Version|Z-Wave Protocol Version|Z-Wave Protocol Version|
|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|
|Application Version|Application Version|Application Version|Application Version|Application Version|Application Version|Application Version|Application Version|
|Application Sub Version|Application Sub Version|Application Sub Version|Application Sub Version|Application Sub Version|Application Sub Version|Application Sub Version|Application Sub Version|



**Z-Wave** **Library** **Type** **(8** **bits)**

CC:0086.01.12.11.001 This field MUST carry the Z-Wave Protocol Library Type.


CC:0086.01.12.11.002 The value MUST comply with Table 3.162.

|Library Type|Table 3.162: Z-Wave Library Type Description|Version|
|---|---|---|
|Library Type|Description|Version|
|0x00|N/A|-|
|0x01|Static Controller|1|
|0x02|Controller|1|
|0x03|Enhanced End Node|1|
|0x04|End Node|1|
|0x05|Installer|1|
|0x06|Routing End Node|1|
|0x07|Bridge Controller|1|
|0x08|Device Under Test (DUT)|1|
|0x09|N/A|1|
|0x0A|AV Remote|1|
|0x0B|AV Device|1|



CC:0086.01.12.11.003 Values marked as not applicable (N/A) MUST be ignored by a receiving node.


CC:0086.01.12.11.004 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Z-Wave** **Protocol** **Version** **&** **Z-Wave** **Protocol** **Sub** **Version**

These fields advertise information specific to Software Development Kits (SDK) provided by stack
manufacturers.


**Application** **Version** **(8** **bits)**


Returns the Application Version and can have values in the range 0 to 255. The manufacturer assigns
the Application Version.


**Application** **Sub** **Version** **(8** **bits)**


Returns the Application Sub Version and can have values in the range 0 to 255. The manufacturer
assigns the Application Sub Version.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 778




<!-- PAGE 780 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.43.5** **Version** **Command** **Class** **Get** **Command**


The Version Command Class Get Command is used to request the individual command class versions
from a device.


CC:0086.01.13.11.001 The Version Command Class Report Command MUST be returned in response to this command.


Only versions from the command classes shown in the NIF, in the Security Command Supported
Report or in the Multi Channel Capability Report can be requested.

It is not possible to get a version number for the Generic and Specific Device Classes.


CC:0086.01.13.11.002 This command MUST NOT be issued via multicast addressing.


CC:0086.01.13.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


The Version Report Command is be used to advertise the library type, protocol version and application
version from a device.


Table 3.163: Version Command Class Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|
|Command = VERSION_COMMAND_CLASS_GET|Command = VERSION_COMMAND_CLASS_GET|Command = VERSION_COMMAND_CLASS_GET|Command = VERSION_COMMAND_CLASS_GET|Command = VERSION_COMMAND_CLASS_GET|Command = VERSION_COMMAND_CLASS_GET|Command = VERSION_COMMAND_CLASS_GET|Command = VERSION_COMMAND_CLASS_GET|
|Requested Command Class|Requested Command Class|Requested Command Class|Requested Command Class|Requested Command Class|Requested Command Class|Requested Command Class|Requested Command Class|



**Requested** **Command** **Class** **(8** **bits)**

This field is used to indicate the Command Class identifier that is being requested.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 779




<!-- PAGE 781 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.43.6** **Version** **Command** **Class** **Report** **Command**


The Version Command Class Report Command is used to report the individual command class versions
from a device.


Table 3.164: Version Command Class Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|
|Command = VERSION_COMMAND_CLASS_REPORT|Command = VERSION_COMMAND_CLASS_REPORT|Command = VERSION_COMMAND_CLASS_REPORT|Command = VERSION_COMMAND_CLASS_REPORT|Command = VERSION_COMMAND_CLASS_REPORT|Command = VERSION_COMMAND_CLASS_REPORT|Command = VERSION_COMMAND_CLASS_REPORT|Command = VERSION_COMMAND_CLASS_REPORT|
|Requested Command Class|Requested Command Class|Requested Command Class|Requested Command Class|Requested Command Class|Requested Command Class|Requested Command Class|Requested Command Class|
|Command Class Version|Command Class Version|Command Class Version|Command Class Version|Command Class Version|Command Class Version|Command Class Version|Command Class Version|



**Requested** **Command** **Class** **(8** **bits)**

The Requested Command Class field specifies what Command Class the returned version belongs to.


**Command** **Class** **Version** **(8** **bits)**

If the requested Command Class is supported, this field is used to return the Command Class Version.
CC:0086.01.14.11.001 This field MUST be in the range 1..255. It starts with 1 and is incremented every time a new version
of the Command Class is released.


CC:0086.01.14.11.002 If the requested Command Class is not supported or controlled, a responding node MUST set the
Command Class Version field to 0x00.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 780

---

<!-- PAGE 782 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.44** **Version** **Command** **Class,** **version** **2**


The Version Command Class, version 2 is extended to report the version of various firmware images
such as a host processor firmware, etc. in addition to the firmware image running in the Z-Wave chip.


As an example, one may construct a product comprising a Z-Wave chip and a secondary host processor
that maintains a security certificate. With Firmware Update Meta Data Command Class, version 3
the Z-Wave chip, the host processor and the security certificate may all be updated via individual
firmware IDs. Version 2 of the Version Command Class (this Command Class) allows a controlling
node to request the corresponding version information for each firmware ID.

Commands not mentioned here remain the same as specified for Version Command Class, version 1.


**3.2.44.1** **Version** **Report** **Command**


This command is used to report the library type, protocol version and application version from a
node.

Version 2 of this command renames the fields Application Version and Application Sub Version to
Firmware 0 Version and Firmware 0 Sub Version. The use remains the same.

CC:0086.02.12.11.001 A node MUST advertise the version of all firmware images which can be updated via the Firmware
Update Command Class.


CC:0086.02.12.11.002 A one-chip system MUST comply with the following:


CC:0086.02.12.11.003 The Firmware 0 Version MUST reflect the complete firmware implementing the Z-Wave protocol
stack as well as the Z-Wave application.


CC:0086.02.12.11.004 A multi-processor system MUST comply with the following:



CC:0086.02.12.11.005


CC:0086.02.12.11.006


CC:0086.02.12.13.001




- The Firmware 0 Version MUST reflect the firmware implementing the Z-Wave protocol stack
and the inter-chip interface module that enables the Z-Wave application to run in the host

processor.

Another firmware number (e.g. Firmware 1) version MUST reflect the Z-Wave application that
runs in the host processor. Any firmware number larger than 0 MAY be used for this purpose.



CC:0086.02.12.13.002 A node MAY advertise the version of additional images hosted by the node; even if such images cannot
be updated via the Firmware Update Command Class.


An illustration is given in Figure 3.27 and Figure 3.28.


Figure 3.27: Version Report::Firmware Numbering


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 781




<!-- PAGE 783 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 3.28: Version Report::Firmware Numbering (2)


Further, version 2 of the Version Report command introduces a Hardware Version field as well as new
version fields for each additional firmware image implemented by the actual device.


Table 3.165: Version Report Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|
|Command = VERSION_REPORT|Command = VERSION_REPORT|Command = VERSION_REPORT|Command = VERSION_REPORT|Command = VERSION_REPORT|Command = VERSION_REPORT|Command = VERSION_REPORT|Command = VERSION_REPORT|
|Z-Wave Protocol Library Type|Z-Wave Protocol Library Type|Z-Wave Protocol Library Type|Z-Wave Protocol Library Type|Z-Wave Protocol Library Type|Z-Wave Protocol Library Type|Z-Wave Protocol Library Type|Z-Wave Protocol Library Type|
|Z-Wave Protocol Version|Z-Wave Protocol Version|Z-Wave Protocol Version|Z-Wave Protocol Version|Z-Wave Protocol Version|Z-Wave Protocol Version|Z-Wave Protocol Version|Z-Wave Protocol Version|
|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|Z-Wave Protocol Sub Version|
|Firmware 0 Version|Firmware 0 Version|Firmware 0 Version|Firmware 0 Version|Firmware 0 Version|Firmware 0 Version|Firmware 0 Version|Firmware 0 Version|
|Firmware 0 Sub Version|Firmware 0 Sub Version|Firmware 0 Sub Version|Firmware 0 Sub Version|Firmware 0 Sub Version|Firmware 0 Sub Version|Firmware 0 Sub Version|Firmware 0 Sub Version|
|Hardware Version<br>|Hardware Version<br>|Hardware Version<br>|Hardware Version<br>|Hardware Version<br>|Hardware Version<br>|Hardware Version<br>|Hardware Version<br>|
|Number of frmware targets|Number of frmware targets|Number of frmware targets|Number of frmware targets|Number of frmware targets|Number of frmware targets|Number of frmware targets|Number of frmware targets|
|Firmware 1 Version|Firmware 1 Version|Firmware 1 Version|Firmware 1 Version|Firmware 1 Version|Firmware 1 Version|Firmware 1 Version|Firmware 1 Version|
|Firmware 1 Sub Version|Firmware 1 Sub Version|Firmware 1 Sub Version|Firmware 1 Sub Version|Firmware 1 Sub Version|Firmware 1 Sub Version|Firmware 1 Sub Version|Firmware 1 Sub Version|
|…|…|…|…|…|…|…|…|
|Firmware N Version|Firmware N Version|Firmware N Version|Firmware N Version|Firmware N Version|Firmware N Version|Firmware N Version|Firmware N Version|
|Firmware N Sub Version|Firmware N Sub Version|Firmware N Sub Version|Firmware N Sub Version|Firmware N Sub Version|Firmware N Sub Version|Firmware N Sub Version|Firmware N Sub Version|



**Z-Wave** **Library** **Type** **(8** **bits)**


For a description, refer to Section 3.2.43.4.


**Z-Wave** **Protocol** **Version** **and** **Z-Wave** **Protocol** **Sub** **Version**

These fields advertise information specific to Software Development Kits (SDK) provided by stack
manufacturers.


**Firmware** **0** **Version** **(8** **bits)**

Returns the Firmware 0 Version. Firmware 0 is dedicated to the Z-Wave chip firmware. The manuCC:0086.02.12.11.007 facturer MUST assign a version number. Previously called Application Version.


**Firmware** **0** **Sub** **Version** **(8** **bits)**

Returns the Firmware 0 Sub Version. Firmware 0 is dedicated to the Z-Wave chip firmware. The
CC:0086.02.12.11.008 manufacturer MUST assign a sub version number. Previously called Application Sub Version.


**Hardware** **Version** **(8** **bits)**



CC:0086.02.12.11.009


CC:0086.02.12.11.00A


CC:0086.02.12.12.001



The Hardware Version field MUST report a value which is unique to this particular version of the
product. The value MUST be updated to a new value every time the hardware is modified for a given
product. The value 0x00 SHOULD NOT be used for the Hardware Version.



CC:0086.02.12.11.00B It MUST be possible to uniquely determine the hardware characteristics from the Hardware Version
field in combination with the Manufacturer ID, Product Type ID and Product ID fields of Manufacturer Specific Info Report of the Manufacturer Specific Command Class.

This information allows a user to pick a firmware image version that is guaranteed to work with this
particular version of the product.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 782




<!-- PAGE 784 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Note that the Hardware Version field is intended for the hardware version of the entire product, not
just the version of the Z-Wave radio chip.


**Number** **of** **Firmware** **Targets** **(8** **bits)**

CC:0086.02.12.11.00C The Number of Firmware Targets field MUST report the number of firmware Version + Sub Version
fields following this field. The Firmware 0 Version fields are not included.

CC:0086.02.12.11.00D The field MUST be zero if the device only implements a Firmware 0 target, the Z-Wave chip.


**Firmware** **Version** **(N** ***** **8** **bits)**


CC:0086.02.12.11.00E Returns the Firmware n Version. The manufacturer MUST assign a unique Firmware n Version.


**Firmware** **Sub** **Version** **(N** ***** **8** **bits)**


CC:0086.02.12.11.00F Returns the Firmware n Sub Version. The manufacturer MUST assign a unique Firmware n Sub
Version.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 783

---

<!-- PAGE 785 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.45** **Version** **Command** **Class,** **version** **3**


The Version Command Class, version 3 allows supporting nodes to advertise capabilities related to the
Version Command Class and optionally provide a detailed list of information regarding implementation
on the Z-Wave chip.


**3.2.45.1** **Compatibility** **considerations**


The Version Command Class, version 3 is backwards compatible with the Version Command Class,
version 2. A node supporting the Version Command Class, version 3 MUST also support the Version
Command Class, version 2.

All commands and fields not described in this version remain unchanged from version 2.


The Version Command Class, version 3 introduces the possibility for a node to advertise its supported
Version Command Class capabilities with the following commands:


 - Version Capabilities Get Command


 - Version Capabilities Report Command


Supporting nodes MUST advertise support for commands present in previous versions of this Command Class for backwards compatibility.


The following commands are optionally implemented by supporting nodes:


 - Version Z-Wave Software Get Command


 - Version Z-Wave Software Report Command


The Version Z-Wave Software Get/Report commands are used to provide detailed information on the
actual software running on the Z-Wave radio SoC.


**3.2.45.2** **Version** **Capabilities** **Get** **Command**


This command is used to request which version commands are supported by a node.


The Version Capabilities Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.166: Version Capabilities Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|
|Command = VERSION_CAPABILITIES_GET|Command = VERSION_CAPABILITIES_GET|Command = VERSION_CAPABILITIES_GET|Command = VERSION_CAPABILITIES_GET|Command = VERSION_CAPABILITIES_GET|Command = VERSION_CAPABILITIES_GET|Command = VERSION_CAPABILITIES_GET|Command = VERSION_CAPABILITIES_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 784




<!-- PAGE 786 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.45.3** **Version** **Capabilities** **Report** **Command**


This command is used to advertise the version commands supported by the sending node.


Table 3.167: Version Capabilities Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|
|Command = VERSION_CAPABILITIES_REPORT|Command = VERSION_CAPABILITIES_REPORT|Command = VERSION_CAPABILITIES_REPORT|Command = VERSION_CAPABILITIES_REPORT|Command = VERSION_CAPABILITIES_REPORT|Command = VERSION_CAPABILITIES_REPORT|Command = VERSION_CAPABILITIES_REPORT|Command = VERSION_CAPABILITIES_REPORT|
|Reserved|Reserved|Reserved|Reserved|Reserved|ZWS|CC|V|



**V** **(Version)** **(1** **bit)**

This field is used to advertise support for the version information queried with the Version Get
Command.

This field MUST be set to 1.


**CC** **(Command** **Class)** **(1** **bit)**

This field is used to advertise support for the Command Class version information queried with the
Version Command Class Get Command.

This field MUST be set to 1.


**ZWS** **(Z-Wave** **Software)** **(1** **bit)**

This field is used to advertise support for the detailed Z-Wave software version information queried
with the Version Z-Wave Software Get Command.


The value 1 MUST indicate that the sending node supports the Version Z-Wave Software Get Command.


The value 0 MUST indicate that the sending node does not support the Version Z-Wave Software Get
Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 785




<!-- PAGE 787 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.45.4** **Version** **Z-Wave** **Software** **Get** **Command**


This command is used to request the detailed Z-Wave chip software version information of a node.


A node advertising no support for detailed Z-Wave software version information in the _Version_ _Ca-_
_pabilities_ _Report_ _Command_ MUST ignore this command.


The _Version_ _Z-Wave_ _Software_ _Report_ _Command_ MUST be returned in response to this command
unless it is to be ignored.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.168: Version Z-Wave Software Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|
|Command = VERSION_ZWAVE_SOFTWARE_GET|Command = VERSION_ZWAVE_SOFTWARE_GET|Command = VERSION_ZWAVE_SOFTWARE_GET|Command = VERSION_ZWAVE_SOFTWARE_GET|Command = VERSION_ZWAVE_SOFTWARE_GET|Command = VERSION_ZWAVE_SOFTWARE_GET|Command = VERSION_ZWAVE_SOFTWARE_GET|Command = VERSION_ZWAVE_SOFTWARE_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 786




<!-- PAGE 788 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.45.5** **Version** **Z-Wave** **Software** **Report** **Command**


This command is used to advertise the detailed Z-Wave chip software version information of a node.


Table 3.169: Version Z-Wave Software Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|Command Class = COMMAND_CLASS_VERSION|
|Command = VERSION_ZWAVE_SOFTWARE_REPORT|Command = VERSION_ZWAVE_SOFTWARE_REPORT|Command = VERSION_ZWAVE_SOFTWARE_REPORT|Command = VERSION_ZWAVE_SOFTWARE_REPORT|Command = VERSION_ZWAVE_SOFTWARE_REPORT|Command = VERSION_ZWAVE_SOFTWARE_REPORT|Command = VERSION_ZWAVE_SOFTWARE_REPORT|Command = VERSION_ZWAVE_SOFTWARE_REPORT|
|SDK version 1 (MSB)|SDK version 1 (MSB)|SDK version 1 (MSB)|SDK version 1 (MSB)|SDK version 1 (MSB)|SDK version 1 (MSB)|SDK version 1 (MSB)|SDK version 1 (MSB)|
|SDK version 2|SDK version 2|SDK version 2|SDK version 2|SDK version 2|SDK version 2|SDK version 2|SDK version 2|
|SDK version 3 (LSB)|SDK version 3 (LSB)|SDK version 3 (LSB)|SDK version 3 (LSB)|SDK version 3 (LSB)|SDK version 3 (LSB)|SDK version 3 (LSB)|SDK version 3 (LSB)|
|Z-Wave Application Framework API Version 1 (MSB)|Z-Wave Application Framework API Version 1 (MSB)|Z-Wave Application Framework API Version 1 (MSB)|Z-Wave Application Framework API Version 1 (MSB)|Z-Wave Application Framework API Version 1 (MSB)|Z-Wave Application Framework API Version 1 (MSB)|Z-Wave Application Framework API Version 1 (MSB)|Z-Wave Application Framework API Version 1 (MSB)|
|Z-Wave Application Framework API Version 2|Z-Wave Application Framework API Version 2|Z-Wave Application Framework API Version 2|Z-Wave Application Framework API Version 2|Z-Wave Application Framework API Version 2|Z-Wave Application Framework API Version 2|Z-Wave Application Framework API Version 2|Z-Wave Application Framework API Version 2|
|Z-Wave Application Framework API Version 3 (LSB)|Z-Wave Application Framework API Version 3 (LSB)|Z-Wave Application Framework API Version 3 (LSB)|Z-Wave Application Framework API Version 3 (LSB)|Z-Wave Application Framework API Version 3 (LSB)|Z-Wave Application Framework API Version 3 (LSB)|Z-Wave Application Framework API Version 3 (LSB)|Z-Wave Application Framework API Version 3 (LSB)|
|Z-Wave Application Framework Build Number 1 (MSB)|Z-Wave Application Framework Build Number 1 (MSB)|Z-Wave Application Framework Build Number 1 (MSB)|Z-Wave Application Framework Build Number 1 (MSB)|Z-Wave Application Framework Build Number 1 (MSB)|Z-Wave Application Framework Build Number 1 (MSB)|Z-Wave Application Framework Build Number 1 (MSB)|Z-Wave Application Framework Build Number 1 (MSB)|
|Z-Wave Application Framework Build Number 2 (LSB)|Z-Wave Application Framework Build Number 2 (LSB)|Z-Wave Application Framework Build Number 2 (LSB)|Z-Wave Application Framework Build Number 2 (LSB)|Z-Wave Application Framework Build Number 2 (LSB)|Z-Wave Application Framework Build Number 2 (LSB)|Z-Wave Application Framework Build Number 2 (LSB)|Z-Wave Application Framework Build Number 2 (LSB)|
|Host Interface Version 1 (MSB)|Host Interface Version 1 (MSB)|Host Interface Version 1 (MSB)|Host Interface Version 1 (MSB)|Host Interface Version 1 (MSB)|Host Interface Version 1 (MSB)|Host Interface Version 1 (MSB)|Host Interface Version 1 (MSB)|
|Host Interface Version 2|Host Interface Version 2|Host Interface Version 2|Host Interface Version 2|Host Interface Version 2|Host Interface Version 2|Host Interface Version 2|Host Interface Version 2|
|Host Interface Version 3 (LSB)|Host Interface Version 3 (LSB)|Host Interface Version 3 (LSB)|Host Interface Version 3 (LSB)|Host Interface Version 3 (LSB)|Host Interface Version 3 (LSB)|Host Interface Version 3 (LSB)|Host Interface Version 3 (LSB)|
|Host Interface Build Number 1 (MSB)|Host Interface Build Number 1 (MSB)|Host Interface Build Number 1 (MSB)|Host Interface Build Number 1 (MSB)|Host Interface Build Number 1 (MSB)|Host Interface Build Number 1 (MSB)|Host Interface Build Number 1 (MSB)|Host Interface Build Number 1 (MSB)|
|Host Interface Build Number 2 (LSB)|Host Interface Build Number 2 (LSB)|Host Interface Build Number 2 (LSB)|Host Interface Build Number 2 (LSB)|Host Interface Build Number 2 (LSB)|Host Interface Build Number 2 (LSB)|Host Interface Build Number 2 (LSB)|Host Interface Build Number 2 (LSB)|
|Z-Wave Protocol Version 1 (MSB)|Z-Wave Protocol Version 1 (MSB)|Z-Wave Protocol Version 1 (MSB)|Z-Wave Protocol Version 1 (MSB)|Z-Wave Protocol Version 1 (MSB)|Z-Wave Protocol Version 1 (MSB)|Z-Wave Protocol Version 1 (MSB)|Z-Wave Protocol Version 1 (MSB)|
|Z-Wave Protocol Version 2|Z-Wave Protocol Version 2|Z-Wave Protocol Version 2|Z-Wave Protocol Version 2|Z-Wave Protocol Version 2|Z-Wave Protocol Version 2|Z-Wave Protocol Version 2|Z-Wave Protocol Version 2|
|Z-Wave Protocol Version 3 (LSB)|Z-Wave Protocol Version 3 (LSB)|Z-Wave Protocol Version 3 (LSB)|Z-Wave Protocol Version 3 (LSB)|Z-Wave Protocol Version 3 (LSB)|Z-Wave Protocol Version 3 (LSB)|Z-Wave Protocol Version 3 (LSB)|Z-Wave Protocol Version 3 (LSB)|
|Z-Wave Protocol Build Number 1 (MSB)|Z-Wave Protocol Build Number 1 (MSB)|Z-Wave Protocol Build Number 1 (MSB)|Z-Wave Protocol Build Number 1 (MSB)|Z-Wave Protocol Build Number 1 (MSB)|Z-Wave Protocol Build Number 1 (MSB)|Z-Wave Protocol Build Number 1 (MSB)|Z-Wave Protocol Build Number 1 (MSB)|
|Z-Wave Protocol Build Number 2 (LSB)|Z-Wave Protocol Build Number 2 (LSB)|Z-Wave Protocol Build Number 2 (LSB)|Z-Wave Protocol Build Number 2 (LSB)|Z-Wave Protocol Build Number 2 (LSB)|Z-Wave Protocol Build Number 2 (LSB)|Z-Wave Protocol Build Number 2 (LSB)|Z-Wave Protocol Build Number 2 (LSB)|
|Application Version 1 (MSB)|Application Version 1 (MSB)|Application Version 1 (MSB)|Application Version 1 (MSB)|Application Version 1 (MSB)|Application Version 1 (MSB)|Application Version 1 (MSB)|Application Version 1 (MSB)|
|Application Version 2|Application Version 2|Application Version 2|Application Version 2|Application Version 2|Application Version 2|Application Version 2|Application Version 2|
|Application Version 3 (LSB)|Application Version 3 (LSB)|Application Version 3 (LSB)|Application Version 3 (LSB)|Application Version 3 (LSB)|Application Version 3 (LSB)|Application Version 3 (LSB)|Application Version 3 (LSB)|
|Application Build Number 1 (MSB)|Application Build Number 1 (MSB)|Application Build Number 1 (MSB)|Application Build Number 1 (MSB)|Application Build Number 1 (MSB)|Application Build Number 1 (MSB)|Application Build Number 1 (MSB)|Application Build Number 1 (MSB)|
|Application Build Number 2 (LSB)|Application Build Number 2 (LSB)|Application Build Number 2 (LSB)|Application Build Number 2 (LSB)|Application Build Number 2 (LSB)|Application Build Number 2 (LSB)|Application Build Number 2 (LSB)|Application Build Number 2 (LSB)|



**SDK** **version** **(24** **bits)**

This field is used to advertise the SDK version used for building the Z-Wave chip software components
for the node.

The value 0 MUST indicate that this field is unused. Other values MUST indicate the SDK version.


**Z-Wave** **Application** **Framework** **API** **Version** **(24** **bits)**

This field is used to advertise the Z-Wave Application Framework API version used by the node.

The value 0 MUST indicate that this field is unused. Other values MUST indicate the Z-Wave
Application Framework API version.


**Z-Wave** **Application** **Framework** **Build** **Number** **(16** **bits)**

This field is used to advertise the Z-Wave Application Framework build number running on the node.

The value 0 MUST indicate that this field is unused. Other values MUST indicate the Z-Wave
Application Framework build number.

This field MUST be set to 0 if the Application Framework API Version field is set to 0.


**Host** **Interface** **Version** **(24** **bits)**

This field is used to advertise the version of the Serial API exposed to a host CPU or a second Chip.

The value 0 MUST indicate that this field is unused. Other values MUST indicate the actual API
version.

This field MUST be set to 0 by a node running on a single chip.


**Host** **Interface** **Build** **Number** **(16** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 787




<!-- PAGE 789 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to advertise the build number of the Serial API software exposed to a host CPU or
second Chip.

The value 0 MUST indicate that this field is unused. Other values MUST indicate the actual API
build number.

This field MUST be set to 0 if the Host Interface Version field is set to 0.


**Z-Wave** **Protocol** **Version** **(24** **bits)**

This field is used to advertise the Z-Wave protocol version used by the node.

This field MUST be set to the same value as the Z-Wave Protocol Version and Z-Wave Protocol Sub
Version fields present in the Version Report Command.

Byte 1 of this field MUST be set to the same value as the Z-Wave Protocol Version field present in
the Version Report Command.

Byte 2 of this field MUST be set to the same value as the Z-Wave Protocol Sub Version field present
in the Version Report Command.


**Z-Wave** **Protocol** **Build** **Number** **(16** **bits)**

This field is used to advertise the actual build number of the Z-Wave protocol software used by the
node.

The value 0 MUST indicate that this field is unused. Other values MUST indicate the Z-Wave protocol
build number.


**Application** **Version** **(24** **bits)**

This field is used to advertise the version of application software used by the node on its Z-Wave chip.

The value 0 MUST indicate that this field is unused. Other values MUST indicate the application
version.

This field MUST be set to 0 by a node if its application is running on a host CPU.


If a supporting node’s application is running on the Z-Wave chip:

 - Byte 1 of this field MUST be set to the same value as the Application Version / Firmware 0
Version field present in the Version Report Command.

 - Byte 2 of this field MUST be set to the same value as the Application Sub Version / Firmware
0 Sub Version field present in the Version Report Command.


**Application** **Build** **Number** **(16** **bits)**

This field is used to advertise the actual build of the application software used by the node on its
Z-Wave chip.

The value 0 MUST indicate that this field is unused. Other values MUST indicate the application
build number.


**3.2.45.5.1** **Version** **fields**


Fields indicating version numbers are composed of 3 bytes. Version fields MUST be used and interpreted in the following manner:

If used, Byte 1 of a version field MUST represent the major version digit.

If used, Byte 2 of a version field MUST represent the minor version digit.

If used, Byte 3 of a version field MUST represent the patch version digit.

For example, if the node used Z-Wave SDK version 6.51.09, it MUST set the SDK version field to
0x063309. Unused bytes MUST be set to 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 788