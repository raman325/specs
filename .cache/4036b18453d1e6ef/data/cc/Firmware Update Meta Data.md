<!-- PAGE 632 -->

CC:007A.01.00.13.001


CC:007A.01.00.12.001



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.15** **Firmware** **Update** **Meta** **Data** **Command** **Class,** **version** **1** **[DEPRECATED]**


**Warning:** **THIS** **VERSION** **HAS** **BEEN** **DEPRECATED**


A device MAY implement support for this version of the command class, but it is RECOMMENDED that new implementations implement the Firmware Update Meta Data Command Class,
version 3.


If implementing support for this version of the command class, it is RECOMMENDED that support
for Firmware Update Meta Data Command Class, version 3 is also implemented.


The Firmware Update Meta Data Command Class may be used to transfer a firmware image to a
Z-Wave device.



CC:007A.01.00.11.001 A device which supports the Firmware Update CC MUST support the Version CC and the Manufacturer Specific CC to enable other devices to select the correct firmware for a specific target. The
Version Command Class may be used to verify that the intended firmware version is installed.


CC:007A.01.00.11.002 Devices implementing the Firmware Update CC MUST support a data rate of 40kbit/s or more.

CC:007A.01.00.12.002 A checksum SHOULD be appended to the firmware image to ensure the integrity of the image. A


CC:007A.01.00.12.003
receiving device SHOULD verify the integrity of the received firmware image by matching the received
firmware image checksum and the firmware image checksum that is indicated by the Firmware Meta
Data Report when the firmware update is initiated.

CC:007A.01.00.12.004 It is RECOMMENDED that firmware update is enabled by out-of-band authentication (e.g. physical
activation of a pushbutton). If out-of-band authentication is implemented, the device to receive a
firmware update must be armed for firmware update before the Firmware Update Meta Data Request
Get Command is issued.


**3.2.15.1** **Firmware** **Meta** **Data** **Get** **Command**


The Firmware Meta Data Get Command is used to request information on the current firmware in
the device.


CC:007A.01.01.11.001 The Firmware Meta Data Report Command MUST be returned in response to this command.


CC:007A.01.01.11.002 This command MUST NOT be issued via multicast addressing.


CC:007A.01.01.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.48: Firmware Meta Data Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_MD_GET|Command = FIRMWARE_MD_GET|Command = FIRMWARE_MD_GET|Command = FIRMWARE_MD_GET|Command = FIRMWARE_MD_GET|Command = FIRMWARE_MD_GET|Command = FIRMWARE_MD_GET|Command = FIRMWARE_MD_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 631




<!-- PAGE 633 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.15.2** **Firmware** **Meta** **Data** **Report** **Command**


The Firmware Meta Data Report Command is used to advertise the status of the current firmware in
the device.


Table 3.49: Firmware Meta Data Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|
|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|



**Manufacturer** **ID** **(16** **bits)**


The Manufacturer ID is a unique ID identifying the manufacturer of the device.

Manufacturer identifiers can be found in [32]

CC:007A.01.02.11.001 The first byte MUST be the most significant byte.


**Firmware** **ID** **(16** **bits)**


CC:007A.01.02.12.001 A manufacturer SHOULD assign a unique Firmware ID to each existing product variant. A product
variant may be a particular hardware version for a particular world region. When combined with the
Manufacturer ID, the Firmware ID is a unique identification of a firmware image that is guaranteed
to work with a particular product among all Z-Wave enabled products in the world.


If the product has no Firmware ID, the value 0x0000 MUST be returned.

CC:007A.01.02.11.002 The first byte MUST be the most significant byte.

A user may request Manufacturer Specific information to get more detailed information on the product.

CC:007A.01.02.12.002 A controlling device SHOULD match the advertised firmware ID for the existing firmware image to
the firmware ID provided for a new image. If the firmware IDs do not match, the controlling device
SHOULD abort the firmware update operation.


**Checksum** **(16** **bits)**

The checksum field is used to report a checksum value of the firmware image currently running in the
CC:007A.01.02.13.001 Z-Wave chip. As an alternative, a value of zero MAY be returned.

CC:007A.01.02.11.003 The first byte MUST be the most significant byte.


CC:007A.01.02.12.003 It is RECOMMENDED to use a checksum algorithm that implements a CRC-CCITT polynomial
using initialization value equal to 0x1D0F and 0x1021 (normal representation).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 632




<!-- PAGE 634 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.15.3** **Firmware** **Update** **Meta** **Data** **Request** **Get** **Command**


The Firmware Update Meta Data Request Get Command is used to request that a firmware update
is initiated.


CC:007A.01.03.11.001 The Firmware Update Meta Data Request Report Command MUST be returned in response to this
command.

CC:007A.01.03.11.002 The firmware update MUST NOT be initiated if the Manufacturer ID and the Firmware ID do not
match the actual firmware image values.


CC:007A.01.03.11.003
The firmware update MUST be aborted if the checksum does not match the calculated checksum after
the firmware image has been transferred.

CC:007A.01.03.12.001 It is RECOMMENDED that firmware update is initiated by out-of-band authentication (e.g. physical
activation of a pushbutton).


CC:007A.01.03.11.004 This command MUST NOT be issued via multicast addressing.


CC:007A.01.03.11.005 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.50: Firmware Update Meta Data Request Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|
|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|



**Manufacturer** **ID** **(16** **bits)**


The Manufacturer ID is a unique ID identifying the manufacturer of the device.

CC:007A.01.03.11.006 Manufacturer identifiers can be found in [32]. The first byte MUST be the most significant byte.


**Firmware** **ID** **(16** **bits)**


CC:007A.01.03.12.002 A manufacturer SHOULD assign a unique Firmware ID to each existing product variant. A product
variant may be a particular hardware version for a particular world region. When combined with the
Manufacturer ID, the Firmware ID is a unique identification of a firmware image that is guaranteed
to work with a particular product among all Z-Wave enabled products in the world.


CC:007A.01.03.11.007
A receiving application MUST check that the Manufacturer ID and Firmware ID fields match the Manufacturer ID and Firmware ID values of the current firmware. While it is NOT RECOMMENDED,
one MAY design a the product that has no Firmware ID.


CC:007A.01.03.11.008 A sending node MUST specify the Firmware ID value 0x0000 to indicate an absent Firmware ID.


CC:007A.01.03.11.009 A receiving node MUST interpret the value 0x0000 as “No Firmware ID available”.

CC:007A.01.03.11.00A The first byte MUST be the most significant byte.


**Checksum** **(16** **bits)**

CC:007A.01.03.11.00B The checksum field MUST carry the checksum of the firmware image about to be transferred.

CC:007A.01.03.11.00C A receiving node MUST match this value and the checksum calculated from the received firmware
image.


CC:007A.01.03.12.004 It is RECOMMENDED to use a checksum algorithm that implements a CRC-CCITT polynomium
using initialization value equal to 0x1D0F and 0x1021 (normal representation). Refer to _CRC-CCITT_
_Source_ _Code_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 633




<!-- PAGE 635 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.15.4** **Firmware** **Update** **Meta** **Data** **Request** **Report** **Command**


This command is used to advertise if the firmware update will be initiated.


Table 3.51: Firmware Update Meta Data Request Report Com
|7|Table 3.5 mand 6|51: Firmwar 5|re Update M 4|Meta Data R 3|Request Repo 2|ort Com- 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|
|Status|Status|Status|Status|Status|Status|Status|Status|



**Status** **(8** **bits)**

CC:007A.01.04.11.001 This field MUST comply with Table 3.81.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 634




<!-- PAGE 636 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.15.5** **Firmware** **Update** **Meta** **Data** **Get** **Command**


The Firmware Update Meta Data Get Command is used to request one or more Firmware Update
Meta Data Report Commands.


CC:007A.01.05.11.001 The Firmware Update Meta Data Report Command MUST be returned in response to this command.



CC:007A.01.05.13.001


CC:007A.01.05.13.002



The transmission of the next Firmware Update Meta Data Get Command MAY be delayed if time is
required to store the most recent firmware fragment in temporary non-volatile memory. A node MAY
request multiple Firmware Update Meta Data Report Commands to improve throughput.



CC:007A.01.05.11.002 This command MUST NOT be issued via multicast addressing.


CC:007A.01.05.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Two exceptions may apply: A noise burst may interfere the transmission or the data source may stop
returning Firmware Update Meta Data Report Commands.


CC:007A.01.05.12.001 To accommodate for bursts of RF noise, a device receiving data SHOULD repeatedly retransmit the
same Firmware Update Meta Data Get Command every 10 seconds in case no Firmware Update Meta
Data Report Commands are received.


CC:007A.01.05.12.002 A device receiving data SHOULD stop retransmitting Firmware Update Meta Data Get commands 2
minutes after the last successful reception of a Firmware Update Meta Data Report Command.


Table 3.52: Firmware Update Meta Data Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|
|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|
|Res|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|
|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|



**Res**

CC:007A.01.05.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Number** **of** **Reports** **(8** **bits)**


Number of Firmware Update Meta Data Report Commands to be received in response to this Firmware
Update Meta Data Get Command.


**Report** **number** **1** **..** **2** **(15** **bits)**

The Report number field indicates the Firmware Update Meta Data Report Command to be requested.
CC:007A.01.05.11.005 The report number values MUST be a sequence starting from 1. The first byte (Report number 1) is
the most significant byte.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 635




<!-- PAGE 637 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.15.6** **Firmware** **Update** **Meta** **Data** **Report** **Command**


The Firmware Update Meta Data Report Command is used to transfer a firmware image fragment.


CC:007A.01.06.11.001 If sending more than a single Firmware Update Meta Data Report Command at a time, a node MUST
apply a delay between each transmitted command. The minimum required time delay and number of
frames before a delay must be inserted depends on the actual bit rate.


      - 40 kbit/s: At least 35 ms if sending more than 1 frame back-to-back


      - 100 kbit/s: At least 15 ms if sending more than 2 frames back-to-back


CC:007A.01.06.12.001 If needed, a controlling node SHOULD abort an ongoing transfer by responding to a Firmware Update
Meta Data Get Command with a Firmware Update Meta Data Report Command with the Last bit
enabled and the Data fields intentionally corrupted.

This will invalidate the calculated firmware checksum, which should eventually cause the receiving
device to return a Firmware Update Meta Data Status Report Command with the status code <check
sum error>.


Table 3.53: Firmware Update Meta Data Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|
|Last|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|
|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|
|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|
|…|…|…|…|…|…|…|…|
|Data N|Data N|Data N|Data N|Data N|Data N|Data N|Data N|



**Last** **(1** **bit)**

The Last flag indicates if the requested Firmware Update Meta Data Report Command carries the
last firmware image fragment.

CC:007A.01.06.11.002 The flag MUST be set to ‘1’ if this is the last fragment. Otherwise the flag MUST be ‘0’.


**Report** **number** **(15** **bits)**

The Report number field indicates the sequence number of the contained firmware fragment. The first
CC:007A.01.06.11.003 firmware fragment MUST be identified by the Report number value 1. The sequence number of each
following firmware fragment MUST be incremented.

Report number 1 is the most significant byte.

The report number may be used to calculate the offset of the data by the formula:

Offset = (Report number – 1) x Number of Data fields (N)

CC:007A.01.06.11.004 Except for the last frame, each Report MUST carry the same number of Data bytes as the first

CC:007A.01.06.13.001 fragment. The last frame MAY carry a shorter Data field.


**Data** **(N** **bytes)**



CC:007A.01.06.11.005


CC:007A.01.06.13.002



The Data field is used to carry one firmware image fragment. Except for the last frame, each Firmware
Update Meta Data Report Command MUST carry the same number of Data bytes as the first fragment. The last frame MAY carry a shorter Data field.



CC:007A.01.06.11.006 A sending device MUST use a fragment size which matches the actual number of available Data bytes.
The number of available Data bytes depends on the actual bit rate, the use of security encapsulation
as well as the presence of Checksum bytes in the Firmware Update Meta Data Report.

CC:007A.01.06.11.007 A receiving device MUST determine the number of Data bytes from the length of the first received
frame.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 636




<!-- PAGE 638 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.15.7** **Firmware** **Update** **Meta** **Data** **Status** **Report** **Command**


This command is used to advertise the firmware update status.

CC:007A.01.07.11.001 The command MUST be issued when the firmware update is completed or aborted by the device
receiving the firmware.

CC:007A.01.07.12.001 A supporting node SHOULD reboot and apply the new firmware image before issuing this command.


CC:007A.01.07.11.002 A node MUST NOT issue Firmware Update Meta Data Get Command after receiving a Firmware
Update Meta Data Status Report.


Table 3.54: Firmware Update Meta Data Status Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|
|Status|Status|Status|Status|Status|Status|Status|Status|



**Status** **(8** **bits)**

CC:007A.01.07.11.003 This field MUST comply with Table 3.71.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 637




<!-- PAGE 639 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.15.8** **Examples**


Figure 3.3 shows a controlling node requesting the Manufacturer ID and Firmware ID of another node
by issuing the Firmware Meta Data Get Command.


Figure 3.3: Requesting Manufacturer ID and Firmware ID of a Node


Figure 3.4 outlines the actual firmware update message flow. Prior to the firmware update, the
supporting node may receive an out-of-band authentication (e.g. physical activation of a pushbutton).
The controller sends a Firmware Meta Data Request Get Command to initiate the downloading a new
firmware image.

The supporting node returns a Firmware Meta Data Request Report Command report to confirm the
update request and the supporting node begins pulling firmware image fragments from the controller.
Finally a Firmware Update Meta Data Status Report is returned to the controller to indicate the
success (or failure) of the update process.


Figure 3.4: Transferring a Firmware Image to a Device


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 638

---

<!-- PAGE 640 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.16** **Firmware** **Update** **Meta** **Data** **Command** **Class,** **version** **2**


Firmware Update Meta Data Command Class, version 2 updates the Firmware Update Meta Data
Report Command.


While support for version 1 has been deprecated, a controlling device implementing Firmware Update
CC:007A.02.00.11.001 Meta Data Command Class, version 2 MUST also be able to control Firmware Update Meta Data
Command Class, version 1 based devices.


**3.2.16.1** **Compatibility** **considerations**


CC:007A.02.00.21.001 A node supporting Firmware Update Meta Data Command Class, version 2 MUST also support
Firmware Update Meta Data Command Class, version 1.

All commands and fields not described in this version remain unchanged from version 1.


**3.2.16.2** **Interoperability** **considerations**


**3.2.16.2.1** **Interoperability** **with** **v1** **devices**


Version 2 of the Firmware Update Meta Data Report command introduces a 16-bit Checksum field
to follow the variable-length Data field. No fields follow the variable-length Data field in Version 1 of
the Firmware Update Meta Data Report command.

At the same time, the specified method for determining the length of the variable-length Data field is
that the length must be calculated from the length of the received frame.


The unintended consequence is that a version 1 implementation receiving a Firmware Update Meta
Data Report v2 command will consider the 16-bit Checksum field to be the last two bytes of the Data
field.


Similarly, a version 2 implementation receiving a Firmware Update Meta Data Report v1 command
will consider the last two bytes of the Data field to be the 16-bit Checksum field.


In either case, the transfer will fail.


CC:007A.02.00.31.001 Therefore, a controlling device implementing the Firmware Update Meta Data Command Class, version 2 MUST do the following when initiating the transfer of a firmware image:


1. Request the version of the Firmware Update Meta Data Command Class from the target device


2. Use the version of the Firmware Update Meta Data Report implemented by the target device

3. Determine the number of Data bytes that can fit into the Firmware Update Meta Data Report
command so that the complete command can still fit into the payload field of the transport
frame. The number of available payload bytes in the frame depends on the actual bit rate, the
use of security encapsulation as well as the presence of Checksum bytes in the Firmware Update
Meta Data Report.


CC:007A.02.00.32.001
The controller SHOULD accept any binary image format and transfer that without any modifications.
The image may be encrypted or carry checksums.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 639




<!-- PAGE 641 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.16.2.2** **Checksum** **calculation**


Version 1 of the Firmware Update Meta Data Command Class introduced a 16-bit Checksum field used
to verify firmware image integrity. It has been a recommendation to use the CRC-CCITT polynomial
for calculating checksums. Nodes having implemented another method for calculating the checksum
will find a non-matching checksum.


From Version 5 onwards, the checksum calculation method is mandatory. For more details about the
checksum calculation, refer to _CRC-CCITT_ _Source_ _Code_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 640




<!-- PAGE 642 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.16.3** **Firmware** **Update** **Meta** **Data** **Report** **Command**


The Firmware Update Meta Data Report command is used to transfer a firmware image fragment.


CC:007A.02.06.11.001 If sending more than a single Firmware Update Meta Data Report Command at a time, a node MUST
apply a delay between each transmitted command. The minimum required time delay and number of
frames before a delay must be inserted depends on the actual bit rate.


      - 40 kbit/s: At least 35 ms if sending more than 1 frame back-to-back


      - 100 kbit/s: At least 15 ms if sending more than 2 frames back-to-back


CC:007A.02.06.12.001 If needed, a controlling node SHOULD abort an ongoing transfer by responding to a Firmware Update
Meta Data Get Command with a Firmware Update Meta Data Report Command with the Last bit
enabled and the Data fields intentionally corrupted while the Checksum field of the Firmware Update
Meta Data Report Command is valid, i.e. calculated over the corrupted Data fields.

This will invalidate the calculated firmware checksum, which should eventually cause the receiving
device to return a Firmware Update Meta Data Status Report Command with the status code <check
sum error>.


Table 3.55: Firmware Update Meta Data Report Command version

|7|Table 3.55 2 6|5: Firmware 5|e Update Met 4|ta Data Repo 3|ort Comman 2|nd version 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|
|Last|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|
|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|
|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|
|…|…|…|…|…|…|…|…|
|Data N|Data N|Data N|Data N|Data N|Data N|Data N|Data N|
|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|
|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|



All fields not described below remain unchanged from version 1.


**Checksum** **(16** **bits)**

CC:007A.02.06.11.002 The checksum field MUST be used to ensure the consistency of the entire command; including the
command class and command identifiers.


CC:007A.02.06.12.002 It is RECOMMENDED to use a checksum algorithm that implements the CRC-CCITT polynomium
using initialization value equal to 0x1D0F and 0x1021 (normal representation).

The Checksum field is known to cause compatibility issues with version 1 devices. Refer to Section
3.2.16.1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 641

---

<!-- PAGE 643 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.17** **Firmware** **Update** **Meta** **Data** **Command** **Class,** **version** **3**


The Firmware Update Meta Data Command Class, version 3 allows a Z-Wave enabled device to receive
one out of several firmware images.


As an example, one may construct a product comprising a Z-Wave chip and a secondary host processor
that maintains a security certificate. With the capability to handle multiple firmware images enables
the Z-Wave chip, the host processor and the security certificate may all be updated via individual
firmware IDs.


**3.2.17.1** **Compatibility** **considerations**


CC:007A.03.00.21.001 A device implementing Firmware Update Meta Data Command Class, version 3 MUST also implement
Firmware Update Meta Data Command Class, version 2.


While support for version 1 has been deprecated, a controlling device implementing Firmware Update
CC:007A.03.00.21.002 Meta Data Command Class, version 2 MUST also be able to control Firmware Update Meta Data
Command Class, version 1 based devices.

All commands and fields not described in this version remain unchanged from version 2.

Note that the minimum granted firmware size that can be transferred using Firmware Update Meta
Data Report command is around 900 kB.


**3.2.17.1.1** **New** **fields** **and** **values**


The Firmware Update Meta Data Command Class, Version 3, introduces WaitTime parameter and a
new Status code 0xFE for the Firmware Update Meta Data Status Report Command.



CC:007A.03.00.21.003



The status code 0xFE is intended for confirming the successful transfer of images which do not
necessitate a restart, e.g. security certificates. If this code was returned to a controller implementing
a previous version, the controller would report that an error had occurred. Therefore, a supporting
node MUST NOT return this code after having updated the firmware image for the Z-Wave chip
image, i.e. the Firmware ID 0 target.


**3.2.17.2** **Interoperability** **considerations**



CC:007A.03.00.32.001 Unintended modification of a firmware image SHOULD be prevented. It is RECOMMENDED that
firmware update is enabled by out-of-band authentication (e.g. physical activation of a pushbutton).


CC:007A.03.00.31.001 A checksum MUST be appended to the Firmware 0 image to ensure the integrity of the image. A

CC:007A.03.00.32.002 receiving device SHOULD verify the integrity of the received Firmware 0 image by matching the
received Firmware 0 image checksum and the Firmware 0 image checksum that is indicated by the
Firmware Meta Data Report when the firmware update is initiated.



CC:007A.03.00.32.003


CC:007A.03.00.31.002



Any image transferred via the Firmware Update Meta Data Command Class SHOULD include a
fingerprint value for validation of the integrity of the entire image after the transfer. The image and
the fingerprint value MUST be packed in one entity which can be stored in one file and transferred
as one entity.



CC:007A.03.00.31.003 A manufacturer MUST assign a unique Firmware ID to each existing product variant. A product
variant may be a particular hardware version for a particular world region. The combination of Manufacturer ID and Firmware ID provides unique identification of a firmware image that is guaranteed
to work with a particular component of a particular product.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 642




<!-- PAGE 644 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.17.2.1** **Interoperability** **with** **v1** **devices**


Version 2 of the Firmware Update Meta Data Report command introduces a 16-bit Checksum field
to follow the variable-length Data field. No fields follow the variable-length Data field in Version 1 of
the Firmware Update Meta Data Report command. Version 3 of the Firmware Update Meta Data
Report command uses the v2 format.

At the same time, the specified method for determining the length of the variable-length Data field is
that the length must be calculated from the length of the received frame.


The unintended consequence is that a version 1 implementation receiving a Firmware Update Meta
Data Report v2 command will consider the 16-bit Checksum field to be the last two bytes of the Data
field.


Similarly, a version 2 implementation receiving a Firmware Update Meta Data Report v1 command
will consider the last two bytes of the Data field to be the 16-bit Checksum field.


In either case, the transfer will fail.


CC:007A.03.00.31.004 Therefore, a node controlling the Firmware Update Meta Data Command Class, version 3 MUST do
the following when initiating the transfer of a firmware image:


1. Request the version of the Firmware Update Meta Data Command Class from the target device


2. Use the version of the Firmware Update Meta Data Report implemented by the target device

3. Determine the number of Data bytes that can fit into the Firmware Update Meta Data Report
command so that the complete command can still fit into the payload field of the transport
frame. The number of available payload bytes in the frame depends on the actual bit rate, the
use of security encapsulation as well as the presence of Checksum bytes in the Firmware Update
Meta Data Report


**3.2.17.2.2** **Checksum** **calculation**


Version 1 of the Firmware Update Meta Data Command Class introduced a 16-bit Checksum field used
to verify firmware image integrity. It has been a recommendation to use the CRC-CCITT polynomial
for calculating checksums. Nodes having implemented another method for calculating the checksum
will find a non-matching checksum.


From Version 5 onwards, the checksum calculation method is mandatory.


For more details about the checksum calculation, refer to _CRC-CCITT_ _Source_ _Code_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 643




<!-- PAGE 645 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.17.3** **Firmware** **Meta** **Data** **Report** **Command**


This command is used to advertise the status of the current firmware in the device.


Table 3.56: Firmware Meta Data Report Command version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|
|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|
|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|
|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|
|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|
|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|
|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|
|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|
|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|
|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|
|…|…|…|…|…|…|…|…|
|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|
|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|



Fields not described below remain unchanged from version 2


**Firmware** **0** **ID** **(16** **bits)**

The Firmware 0 ID field is dedicated to target 0, i.e. the Z-Wave chip.


CC:007A.03.02.11.001 A manufacturer MUST assign a unique Firmware ID to each existing product variant. A product
variant may be a particular hardware version for a particular world region. The combination of Manufacturer ID and Firmware ID provides unique identification of a firmware image that is guaranteed
to work with a particular component of a particular product.

CC:007A.03.02.11.002 The first byte MUST be the most significant byte.

A user may request Manufacturer Specific information to get more detailed information on the product.

CC:007A.03.02.12.001 A controlling node SHOULD match the advertised firmware ID for the existing firmware image to
the firmware ID provided for a new image. If the firmware IDs do not match, the controlling device
SHOULD abort the firmware update operation.


**Firmware** **0** **Checksum** **(16** **bits)**

CC:007A.03.02.11.003 The checksum field is used to ensure consistency of the Firmware 0 image currently in the device.

Supporting nodes MAY set this field to 0x00. In this case the field is unused.


Values in the range 0x0001..0xFFFF indicate that the supporting node advertises the checksum of its
firmware image.

CC:007A.03.02.11.004 The first byte MUST be the most significant byte.


CC:007A.03.02.12.002 It is RECOMMENDED to use a checksum algorithm that implements a CRC-CCITT polynomial
using initialization value equal to 0x1D0F and 0x1021 (normal representation).


**Firmware** **Upgradable** **(8** **bits)**

This field defines whether the Z-Wave chip is firmware upgradable.

CC:007A.03.02.11.005 The value 0x00 MUST indicate that the firmware 0 image is not upgradable.

The value 0xFF MUST indicate that the firmware 0 image is upgradable.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 644




<!-- PAGE 646 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Number** **of** **Firmware** **Targets** **(8** **bits)**

CC:007A.03.02.11.006 The Number of Firmware Targets field MUST report the number of firmware IDs following this field.

CC:007A.03.02.11.007 The Firmware 0 ID field is not included. The field MUST be zero if the device only implements a
Firmware 0 target, i.e. the Z-Wave chip.


**Max** **Fragment** **Size** **(16** **bits)**

CC:007A.03.02.11.008 The Max Fragment Size field MUST report the maximum number of Data bytes that a device is able

CC:007A.03.02.13.001 to receive at a time. A sending node MAY send shorter fragments. The fragment size actually used is
indicated in the Firmware Update Meta Data Request Get Command and confirmed in the Firmware
Update Meta Data Request Report Command.


The Max Fragment Size may be longer than the supported frame length of Z-Wave if the image is to
CC:007A.03.02.11.009 be transferred over e.g. IP. If the image is to be transferred over Z-Wave, the sending node MUST use
a fragment size which matches the actual number of available Data bytes. The number of available
Data bytes depends on the actual bit rate, the use of security encapsulation as well as the presence of
Checksum bytes in the Firmware Update Meta Data Report.


**Firmware** **n** **ID** **(16** **bits)**

CC:007A.03.02.11.00A The Firmware 1 ID field indicates the Firmware ID that MUST be used for target 1. The Firmware
2 ID field represents target 2. And so on.

CC:007A.03.02.11.00B The first byte MUST be the most significant byte.

CC:007A.03.02.12.003 A controlling device SHOULD match the advertised firmware ID for the existing firmware image to
the firmware ID provided for a new image. If the firmware IDs do not match, the controlling device
SHOULD abort the firmware update operation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 645




<!-- PAGE 647 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.17.4** **Firmware** **Update** **Meta** **Data** **Request** **Get** **Command**


The Firmware Update Meta Data Request Get Command is used to request that a firmware update
is initiated by the node receiving this command.


CC:007A.03.03.11.001 The Firmware Update Meta Data Request Report Command MUST be returned in response to this
command.


CC:007A.03.03.11.002 This command MUST NOT be issued via multicast addressing.


CC:007A.03.03.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

CC:007A.03.03.11.004 The firmware update MUST NOT be initiated if the Manufacturer ID and the Firmware ID do not
match the actual firmware image values for the specified Firmware Target.


CC:007A.03.03.11.005
The firmware update MUST be aborted if the checksum does not match the calculated checksum after
the firmware image has been transferred.

CC:007A.03.03.12.001 It is RECOMMENDED that firmware update is enabled by out-of-band authentication (e.g. physical
activation of a pushbutton) prior to the transmission of this command.



CC:007A.03.03.12.002


CC:007A.03.03.11.006



Any image transferred via the Firmware Update Meta Data Command Class SHOULD include a
fingerprint value to enable the validation of the integrity of the entire image after the transfer. The
image and the fingerprint value MUST be packed in one entity which can be stored in one file and
transferred as one entity.


Table 3.57: Firmware Meta Data Request Get Command version

|7|Table 3.5 3 6|57: Firmware 5|e Meta Data 4|a Request G 3|Get Command 2|d version 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|
|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|
|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|
|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|
|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|



All fields not described below remain unchanged from version 2.


**Firmware** **ID** **(16** **bits)**



CC:007A.03.03.11.007 The Firmware ID MUST match the specified target of the actual device.


CC:007A.03.03.11.008
The firmware update MUST NOT be initiated if the Firmware ID does not match the specified target
of the actual device.

CC:007A.03.03.11.009 The first byte MUST be the most significant byte.


**Firmware** **Target** **(8** **bits)**

CC:007A.03.03.11.00A This field MUST be used to identify the firmware image to be updated. The firmware images MUST
be identified as follows:


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 646




<!-- PAGE 648 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|Firmware Target|Table 3.58: Firmware Target (8 bits) Description|
|---|---|
|Firmware Target|Description|
|0x00|Firmware image targeted for the Z-Wave chip.<br>|
|0x01|Firmware image intended for target 1 defned by the manufacturer.|
|…|…<br>|
|0xFF|Firmware image intended for target 255 defned by the manufacturer.|



**Fragment** **Size** **(16** **bits)**

CC:007A.03.03.11.00B The Fragment Size field MUST report the fragment size that is to be used for firmware fragments.
A receiving device MUST use this fragment size for the firmware update. The fragment size is not
exchanged during the actual firmware update.


CC:007A.03.03.11.00C The Fragment Size MUST NOT exceed the Max Fragment Size value of the Firmware Meta Data
Report.

A version 1 Firmware Update Meta Data Request Get Command does not carry a Fragment Size field.
CC:007A.03.03.11.00D A receiving node MUST determine the number of Data bytes from the length of the first received
frame, the use of security encapsulation as well as the presence of Checksum bytes in the Firmware
Update Meta Data Report.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 647




<!-- PAGE 649 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.17.5** **Firmware** **Update** **Meta** **Data** **Request** **Report** **Command**


This command is used to advertise if the firmware update will be initiated.


Table 3.59: Firmware Update Meta Data Request Report Command version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|
|Status|Status|Status|Status|Status|Status|Status|Status|



**Status** **(8** **bits)**

CC:007A.03.04.11.001 This field MUST comply with Table 3.81.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 648




<!-- PAGE 650 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.17.6** **Firmware** **Update** **Meta** **Data** **Get** **Command**


The Firmware Update Meta Data Get Command is used to request one or more Firmware Update
Meta Data Report Commands.


CC:007A.03.05.11.001 One or more Firmware Update Meta Data Report Commands MUST be returned in response to this
command.


CC:007A.03.05.11.002 This command MUST NOT be issued via multicast addressing.


CC:007A.03.05.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

CC:007A.03.05.11.004 A node MUST verify the Manufacturer ID and Firmware ID fields received in a Firmware Update
Meta Data Request Get Command before sending any Firmware Update Meta Data Get Commands.


CC:007A.03.05.11.005 A controlling node receiving a Firmware Update Meta Data Get Command MUST return fragments
of the firmware image that was previously identified by the Manufacturer ID and Firmware ID fields
received in a Firmware Update Meta Data Request Get Command.


CC:007A.03.05.13.001 The transmission of the next Firmware Update Meta Data Get Command MAY be delayed if time is

CC:007A.03.05.13.002 required to store the most recent firmware fragment in temporary non-volatile memory. A node MAY
request multiple Firmware Update Meta Data Report Commands to improve throughput.


CC:007A.03.05.13.003 RAM may be a limited resource. A node MAY adjust the size of incoming Firmware Update Meta
Data Report Commands to the available first level RAM receive buffer by reporting the desired Max
Fragment Size when returning a Firmware Meta Data Report Command in response to a Firmware
Update Meta Data Get Command.


Two exceptions may apply: A noise burst may interfere the transmission or the data source may stop
returning Firmware Update Meta Data Report Commands.


CC:007A.03.05.12.001 To accommodate for bursts of RF noise, a device receiving data SHOULD repeatedly retransmit the
same Firmware Update Meta Data Get Command every 10 seconds in case no Firmware Update Meta
Data Report Commands are received.


CC:007A.03.05.12.002 A device receiving data SHOULD stop retransmitting Firmware Update Meta Data Get commands 2
minutes after the last successful reception of a Firmware Update Meta Data Report Command.


Table 3.60: Firmware Update Meta Data Get Command version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|Command = FIRMWARE_UPDATE_MD_GET|
|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|
|Res|Report Number 1|Report Number 1|Report Number 1|Report Number 1|Report Number 1|Report Number 1|Report Number 1|
|Report Number 2|Report Number 2|Report Number 2|Report Number 2|Report Number 2|Report Number 2|Report Number 2|Report Number 2|



**Res**

CC:007A.03.05.11.006 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Number** **of** **Reports** **(8** **bits)**


Number of Firmware Update Meta Data Report Commands to be received in response to a single
Firmware Update Meta Data Get Command.


CC:007A.03.05.11.007 The requesting node MUST keep track of missing Firmware Update Meta Data Report Commands.


**Report** **Number** **(15** **bits)**

The Report number field indicates the sequence number of the requested firmware fragment. The first
CC:007A.03.05.11.008 firmware fragment MUST be identified by the Report Number value 1.

CC:007A.03.05.11.009 Report number 1 MUST be the most significant byte.


CC:007A.03.05.11.00A


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 649




<!-- PAGE 651 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If the Number of Reports field is larger than 1, the Report Number MUST identify the first firmware
fragment in the requested sequence of firmware fragments.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 650




<!-- PAGE 652 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.17.7** **Firmware** **Update** **Meta** **Data** **Report** **Command**


The Firmware Update Meta Data Report command is used to transfer a firmware image fragment.


CC:007A.03.06.11.001 If sending more than a single Firmware Update Meta Data Report Command at a time, a node MUST
apply a delay between each transmitted command. The minimum required time delay and number of
frames before a delay must be inserted depends on the actual bit rate.


      - 40 kbit/s: At least 35 ms if sending more than 1 frame back-to-back


      - 100 kbit/s: At least 15 ms if sending more than 2 frames back-to-back

After receiving all Firmware Update Meta Data Report Commands required for a complete firmware
image, a receiving node MUST store the firmware image in the Firmware Target specified in a previously received Firmware Update Meta Data Request Get Command.


CC:007A.03.06.12.001 If needed, a controlling node SHOULD abort an ongoing transfer by responding to a Firmware Update
Meta Data Get Command with a Firmware Update Meta Data Report Command with the Last bit
enabled and the Data fields intentionally corrupted while the Checksum field of the Firmware Update
Meta Data Report Command is valid, i.e. calculated over the corrupted Data fields.

This will invalidate the calculated firmware checksum, which should eventually cause the receiving
device to return a Firmware Update Meta Data Status Report Command with the status code <check
sum error>.


Table 3.61: Firmware Update Meta Report Command version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|Command = FIRMWARE_UPDATE_MD_REPORT|
|Last|Report Number 1|Report Number 1|Report Number 1|Report Number 1|Report Number 1|Report Number 1|Report Number 1|
|Report Number 2|Report Number 2|Report Number 2|Report Number 2|Report Number 2|Report Number 2|Report Number 2|Report Number 2|
|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|
|…|…|…|…|…|…|…|…|
|Data N|Data N|Data N|Data N|Data N|Data N|Data N|Data N|
|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|
|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|



All fields not described below remain unchanged from version 2.


**Last** **(1** **bit)**

This field indicates if the Firmware Update Meta Data Report Command is the last one.

CC:007A.03.06.11.002 The value 1 MUST indicate that this is the last report. Otherwise the field MUST be set to 0.


CC:007A.03.06.11.003 On the reception of the last image fragment, the receiving node MUST verify that the transferred
image does match the indicated Manufacturer ID, Firmware ID and Firmware Target values.


**Checksum** **(16** **bits)**

CC:007A.03.06.11.004 The checksum field MUST be used to ensure the consistency of the entire command; including the
command class and command identifiers.


CC:007A.03.06.12.002 It is RECOMMENDED to use a checksum algorithm that implements the CRC-CCITT polynomium
using initialization value equal to 0x1D0F and 0x1021 (normal representation).


CC:007A.03.06.11.005 The checksum algorithm used for the Firmware Update Meta Data Command Class, version 3 MUST
be the same as the algorithm used for the Firmware Update Meta Data Command Class, version 2 in
the actual product.

The Checksum field is known to cause compatibility issues with version 1 devices. Refer to Section
3.2.16.1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 651




<!-- PAGE 653 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.17.8** **Firmware** **Update** **Meta** **Data** **Status** **Report** **Command**


This command is used to advertise the firmware update status.

CC:007A.03.07.11.001 The command MUST be issued when the firmware update is completed or aborted by the device
receiving the firmware.


CC:007A.03.07.11.002 A node MUST NOT issue the Firmware Update Meta Data Get Command after receiving a Firmware
Update Meta Data Status Report.


Table 3.62: Firmware Update Meta Data Status Report Command

|7|Table 3.62 version 3 6|2: Firmware 5|e Update Met 4|ta Data Stat 3|tus Report C 2|Command 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|
|Status|Status|Status|Status|Status|Status|Status|Status|
|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|
|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|



**Status** **(8** **bits)**

CC:007A.03.07.11.003 This field MUST comply with Table 3.71.

CC:007A.03.07.13.001 The status code 0xFE MAY be used for confirming the successful transfer of images which do not
necessitate a restart, e.g. security certificates.


CC:007A.03.07.11.004 The status code 0xFE MUST NOT be advertised after the transfer of an image for the Firmware ID
0 target (the “Z-Wave chip” image).



CC:007A.03.07.11.005



Controlling nodes implementing earlier versions of the Firmware Update Meta Data CC do not support
status codes defined for newer versions. Therefore, a node returning the Firmware Update Meta Data
Status Report Command MUST comply with the version implemented on the controlling device
(device sending the image). The device returning the Firmware Update Meta Data Status Report can
identify the version of the controlling device based on the Firmware Update Meta Data Request Get.
This may be done as follows:


 - If the Firmware Update Meta Data Request Get does not include Firmware Target and Fragment
Size (8 bytes), the controller is version 1 or 2


 - If the Firmware Update Meta Data Request Get includes Firmware Target and Fragment Size
but not Activation (11 bytes), the controller is version 3


**WaitTime** **(16** **bits)**



CC:007A.03.07.11.006 The WaitTime field MUST report the time that is needed before the receiving node again becomes
available for communication after the transfer of an image. The unit is the second.


CC:007A.03.07.11.007 The value 0 (zero) MUST indicate that the node is ready (it SHOULD have rebooted if needed and
applied the Firmware Image).


The value 0xFFFF is reserved and MUST NOT be returned.



CC:007A.03.07.12.001


CC:007A.03.07.12.002



A controlling node receiving this command SHOULD wait for the number of seconds specified in
this field before trying to resume communication. When resuming communication, the controlling
application SHOULD issue a NOP command and wait for acknowledgement.



CC:007A.03.07.13.002 The controlling application MAY attempt resuming communication repeatedly. In that case, the NOP

CC:007A.03.07.11.008 interval SHOULD be five seconds and MUST be at least one second.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 652

---

<!-- PAGE 654 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.18** **Firmware** **Update** **Meta** **Data** **Command** **Class,** **version** **4**


The Firmware Update Meta Data Command Class may be used to transfer a firmware image to a
Z-Wave device.


**3.2.18.1** **Compatibility** **considerations**


All commands and fields not described in this version remain unchanged from version 3.


CC:007A.04.00.21.001 A device implementing Firmware Update Meta Data Command Class, version 4 MUST also implement
Firmware Update Meta Data Command Class, versions 3.


CC:007A.04.00.21.002 While support for version 1 has been deprecated, a controlling device implementing Firmware Update
Meta Data Command Class, version 2 MUST also be able to control Firmware Update Meta Data
Command Class, version 1 based devices.


**3.2.18.1.1** **New** **commands,** **fields** **and** **values**


The Firmware Update Meta Data Command Class version 4 supports delaying and scheduling a
firmware update after downloading the image.


Version 4 updates the Firmware Update Meta Data Request Get Command and introduces the following commands:


      - New Firmware Update Activation Set Command


      - New Firmware Update Activation Status Report


After downloading an image, a device may use the Firmware Update Meta Data Status Report
Command to indicate to the controlling device that the device is waiting for an activation command.


**3.2.18.2** **Interoperability** **considerations**


**3.2.18.2.1** **Interoperability** **with** **v1** **devices**


Version 2 of the Firmware Update Meta Data Report command introduces a 16-bit Checksum field
to follow the variable-length Data field. No fields follow the variable-length Data field in Version 1 of
the Firmware Update Meta Data Report command. Version 4 of the Firmware Update Meta Data
Report command uses the v2 format.

At the same time, the specified method for determining the length of the variable-length Data field is
that the length must be calculated from the length of the received frame.


The unintended consequence is that a version 1 implementation receiving a Firmware Update Meta
Data Report v2 command will consider the 16-bit Checksum field to be the last two bytes of the Data
field.


Similarly, a version 2 implementation receiving a Firmware Update Meta Data Report v1 command
will consider the last two bytes of the Data field to be the 16-bit Checksum field.


In either case, the transfer will fail.


Therefore, a controlling device implementing the Firmware Update Meta Data Command Class, verCC:007A.04.00.31.001 sion 2 MUST do the following when initiating the transfer of a firmware image:


1. Request the version of the Firmware Update Meta Data Command Class from the target device


2. Use the version of the Firmware Update Meta Data Report implemented by the target device

3. Determine the number of Data bytes that can fit into the Firmware Update Meta Data Report
command so that the complete command can still fit into the payload field of the transport
frame. The number of available payload bytes in the frame depends on the actual bit rate, the


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 653




<!-- PAGE 655 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


use of security encapsulation as well as the presence of Checksum bytes in the Firmware Update
Meta Data Report


**3.2.18.2.2** **Checksum** **calculation**


Version 1 of the Firmware Update Meta Data Command Class introduced a 16-bit Checksum field used
to verify firmware image integrity. It has been a recommendation to use the CRC-CCITT polynomial
for calculating checksums. Nodes having implemented another method for calculating the checksum
will find a non-matching checksum.


From Version 5 onwards, the checksum calculation method is mandatory.


For more details about the checksum calculation, refer to _CRC-CCITT_ _Source_ _Code_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 654




<!-- PAGE 656 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.18.3** **Firmware** **Update** **Meta** **Data** **Request** **Get** **Command**


Table 3.63: Firmware Update Meta Data Request Get Command
version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|
|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|
|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|
|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|
|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Activation|



All fields not described below remain unchanged from version 3.


**Activation** **(1** **bit)**

The Activation field is used to advertise if the receiving node may delay the actual firmware update.

CC:007A.04.03.11.001 The field MUST be interpreted as:



CC:007A.04.03.13.001


CC:007A.04.03.11.002




- ’1’: The receiving device MAY delay the actual firmware update.

If the receiving node delays the firmware update, the delay MUST be advertised via the
Status code 0xFD in the Firmware Update Meta data Status Report Command.



CC:007A.04.03.11.003 - ’0’: The receiving device MUST NOT delay the firmware update.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 655




<!-- PAGE 657 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.18.4** **Firmware** **Update** **Meta** **Data** **Status** **Report** **Command**


This command is used to advertise the firmware update status.

CC:007A.04.07.11.001 The command MUST be issued when the firmware update is completed or aborted by the device
receiving the firmware.


CC:007A.04.07.11.002 A node MUST NOT issue the Firmware Update Meta Data Get Command after receiving a Firmware
Update Meta Data Status Report.


Table 3.64: Firmware Update Meta Data Status Report Command

|7|Table 3.64 version 4 6|4: Firmware 5|e Update Met 4|ta Data Stat 3|tus Report C 2|Command 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|
|Status|Status|Status|Status|Status|Status|Status|Status|
|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|
|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|



All fields not described below remain unchanged from version 3.


**Status** **(8** **bits)**

CC:007A.04.07.11.003 This field MUST comply with Table 3.71.

CC:007A.04.07.13.001 The status code 0xFD MAY be used by a version 4 device for confirming that an image has been
successfully transferred but that the actual firmware update will not be performed until a Firmware
Update Activation Set Command is received.


CC:007A.04.07.13.002 The Firmware Update Activation Set Command MAY be delayed for any period of time. The delay
may be controlled via the Schedule Command Class.


CC:007A.04.07.13.003
The status code 0xFE MAY be used for confirming the successful transfer of an image which does not
necessitate a restart, e.g. security a certificate.


CC:007A.04.07.11.004 The status code 0xFE MUST NOT be advertised after the transfer of an image for the Firmware ID
0 target (the “Z-Wave chip” image).



CC:007A.04.07.11.005



Controlling nodes implementing earlier versions of the Firmware Update Meta Data CC do not support
status codes defined for newer versions. Therefore, a node returning the Firmware Update Meta Data
Status Report Command MUST comply with the version implemented on the controlling device
(device sending the image). The device returning the Firmware Update Meta Data Status Report can
identify the version of the controlling device based on the Firmware Update Meta Data Request Get.
This may be done as follows:


 - If the Firmware Update Meta Data Request Get does not include Firmware Target and Fragment
Size (8 bytes), the controller is version 1 or 2


 - If the Firmware Update Meta Data Request Get includes Firmware Target and Fragment Size
but not Activation (11 bytes), the controller is version 3


 - If the Firmware Update Meta Data Request Get includes Activation (12 bytes), the controller
is version 4


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 656




<!-- PAGE 658 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.18.5** **Firmware** **Update** **Activation** **Set** **Command**


This command is used to initiate the programming of a previously transferred firmware image. Refer
to the Firmware Update Meta Data Status Report Command Status code 0xFD.


CC:007A.04.08.13.001 This command MAY be issued directly by a controlling node or MAY be scheduled for later execution
via the Schedule Command Class.


CC:007A.04.08.11.001 The Firmware Update Activation Status Report Command MUST be returned in response to this
command.


Table 3.65: Firmware Update Activation Set Command version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|
|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|
|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|



For fields’ description, refer to the Firmware Update Meta Data Request Get Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 657




<!-- PAGE 659 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.18.6** **Firmware** **Update** **Activation** **Status** **Report**


This command is used to advertise the result of a firmware update operation initiated by the Firmware
Update Activation Set Command.

CC:007A.04.09.11.001 The Firmware Update Activation Status Report fields MUST reflect the values specified in the
Firmware Update Activation Set Command.


Table 3.66: Firmware Update Activation Status Report Command
version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|
|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|
|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|
|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|



For fields not described below, refer to the Firmware Update Meta Data Request Get Command.


**Firmware** **Update** **Status** **(8** **bits)**

CC:007A.04.09.11.002 This field MUST comply with Table 3.74.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 658

---

<!-- PAGE 660 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.19** **Firmware** **Update** **Meta** **Data** **Command** **Class,** **version** **5**


The Firmware Update Meta Data Command Class may be used to transfer a firmware image to or
from a Z-Wave node.


**3.2.19.1** **Compatibility** **considerations**


CC:007A.05.00.21.001 A device implementing Firmware Update Meta Data Command Class, version 5 MUST also implement
Firmware Update Meta Data Command Class, version 4.


Firmware Update Meta Data Command Class, version 5 is backwards compatible with Firmware
Update Meta Data Command Class, version 4.

All commands and fields not mentioned in this version remain unchanged from version 4.


**3.2.19.1.1** **New** **commands,** **fields** **and** **values**


The Firmware Update Meta Data Command Class, version 5 introduces the support of a hardware
identifier to uniquely identify firmware images that can be loaded on devices. This allows devices
running identical software version on different hardware revisions to receive the correct firmware
image.


The following commands are extended from version 4:


      - Firmware Meta Data Report Command


      - Firmware Update Meta Data Request Get Command


      - Firmware Update Meta Data Request Report Command


      - Firmware Update Meta Data Status Report Command


      - Firmware Update Activation Set Command


      - Firmware Update Activation Status Report Command

The Firmware Update Meta Data Command Class, version 5 also introduces the support firmware
download from the Z-Wave node to the controller.


The following commands are introduced:


      - Firmware Update Meta Data Prepare Get Command


      - Firmware Update Meta Data Prepare Report Command


**3.2.19.2** **Interoperability** **Considerations**


**3.2.19.2.1** **Interoperability** **with** **v1** **devices**


Version 2 of the Firmware Update Meta Data Report command introduces a 16-bit Checksum field
to follow the variable-length Data field. No fields follow the variable-length Data field in Version 1 of
the Firmware Update Meta Data Report command. Version 5 of the Firmware Update Meta Data
Report command uses the version 2 format.

At the same time, the specified method for determining the length of the variable-length Data field is
that the length must be calculated from the length of the received frame.


The unintended consequence is that a version 1 implementation receiving a Firmware Update Meta
Data Report version 2 Command will consider the 16-bit Checksum field to be the last two bytes of
the Data field.


Similarly, a version 2 implementation receiving a Firmware Update Meta Data Report version 1
Command will consider the last two bytes of the Data field to be the 16-bit Checksum field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 659




<!-- PAGE 661 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


In either case, the transfer will fail.


Therefore, a controlling device implementing the Firmware Update Meta Data Command Class, verCC:007A.0500.31.001 sion 2 MUST do the following when initiating the transfer of a firmware image:


1. Request the version of the Firmware Update Meta Data Command Class from the target device


2. Use the version of the Firmware Update Meta Data Report implemented by the target device

3. Determine the number of Data bytes that can fit into the Firmware Update Meta Data Report
command so that the complete command can still fit into the payload field of the transport
frame. The number of available payload bytes in the frame depends on the actual bit rate, the
use of security encapsulation as well as the presence of Checksum bytes in the Firmware Update
Meta Data Report


**3.2.19.2.2** **Checksum** **calculation**


Version 1 of the Firmware Update Meta Data Command Class introduced a 16-bit Checksum field used
to verify firmware image integrity. It has been a recommendation to use the CRC-CCITT polynomial
for calculating checksums. There is no way to identify what method has been used for calculating the
checksum for nodes implementing version 1 to version 4. Nodes having implemented another method
for calculating the checksum will find a non-matching checksum.


From Version 5 onwards, the checksum calculation method is mandatory.


For more details about the checksum calculation, refer to _CRC-CCITT_ _Source_ _Code_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 660




<!-- PAGE 662 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.19.3** **Firmware** **Meta** **Data** **Report** **Command**


This command is used to advertise the status of the current firmware in the device.


Table 3.67: Firmware Meta Data Report Command version 5

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|
|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|
|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|
|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|
|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|
|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|
|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|
|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|
|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|
|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|
|…|…|…|…|…|…|…|…|
|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|
|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|
|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|



All fields not described below remain unchanged from version 4.


**Firmware** **0** **Checksum** **(16** **bits)**

The checksum field is used to carry the checksum of the Firmware 0 Image.

CC:007A.05.02.13.001 Supporting nodes MAY set this field to 0x00. In this case the field is unused.


CC:007A.05.02.11.006 Values in the range 0x0001..0xFFFF indicate that the supporting node MUST advertise the checksum
of its firmware 0 image.


CC:007A.05.02.11.001 The checksum MUST be calculated using the CRC-CCITT polynomium using initialization value
equal to 0x1D0F and 0x1021 (normal representation).


For more details, refer to _CRC-CCITT_ _Source_ _Code_ .


**Hardware** **Version** **(8** **bits)**

CC:007A.05.02.11.002 This field MUST report a value which is unique to this particular version of the product.

CC:007A 05.02.11.003 It MUST be possible to uniquely identify applicable firmware images via the Manufacturer ID,
Firmware ID and the Hardware Version fields. This information allows selecting a firmware image
that is guaranteed to work with this particular version of the product.

CC:007A.05.02.11.004 The Hardware Version field MUST apply to the entire product and not only to the version of the
Z-Wave radio chip.

CC:007A.05.02.11.005 This field MUST report the same value as the Version CC Version Report Command: Hardware
Version field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 661




<!-- PAGE 663 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.19.4** **Firmware** **Update** **Meta** **Data** **Request** **Get** **Command**


This command is used to request that a firmware update is initiated by the node receiving this
command.


Table 3.68: Firmware Update Meta Data Request Get Command
version 5

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|
|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|
|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|
|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|
|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Activation|
|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|



All fields not described below remain unchanged from version 4.


**Firmware** **Checksum** **(16** **bits)**

CC:007A.05.03.11.001 The checksum field MUST carry the checksum of the firmware image about to be transferred.


CC:007A.05.03.11.002 The checksum MUST be calculated using the CRC-CCITT polynomium using initialization value
equal to 0x1D0F and 0x1021 (normal representation).


For more details, refer to _CRC-CCITT_ _Source_ _Code_ .


**Hardware** **Version** **(8** **bits)**


Refer to Section 3.2.19.3 Firmware Meta Data Report Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 662




<!-- PAGE 664 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.19.5** **Firmware** **Update** **Meta** **Data** **Request** **Report** **Command**


This command is used to advertise if the firmware update will be initiated.


Table 3.69: Firmware Update Meta Data Request Report Command version 5

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|
|Status|Status|Status|Status|Status|Status|Status|Status|



**Status** **(8** **bits)**

CC:007A.05.04.11.001 This field MUST comply with Table 3.81.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 663




<!-- PAGE 665 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.19.6** **Firmware** **Update** **Meta** **Data** **Status** **Report** **Command**


This command is used to advertise the firmware update status.

CC:007A.05.07.11.001 The command MUST be issued when the firmware update is completed or aborted by the device
receiving the firmware.


CC:007A.05.07.11.002 A device MUST NOT issue the Firmware Update Meta Data Get Command after receiving a Firmware
Update Meta Data Status Report.


Table 3.70: Firmware Update Meta Data Status Report Command

|7|Table 3.70 version 5 6|0: Firmware 5|e Update Met 4|ta Data Stat 3|tus Report C 2|Command 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT|
|Status|Status|Status|Status|Status|Status|Status|Status|
|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|WaitTime MSB|
|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|WaitTime LSB|



All fields not described below are the same as in version 4.


**Status** **(8** **bits)**

CC:007A.05.07.11.003 This field MUST comply with Table 3.71.

CC:007A.05.07.13.001 The status code 0xFD MAY be used by a version 4 device for confirming that an image has been
successfully transferred but that the actual firmware update will not be performed until a Firmware
Update Activation Set Command is received.


CC:007A.05.07.13.002 The Firmware Update Activation Set Command MAY be delayed for any period of time. The delay
may be controlled via the Schedule Command Class.


CC:007A.05.07.13.003
The status code 0xFE MAY be used for confirming the successful transfer of an image which does not
necessitate a restart, e.g. security a certificate.


CC:007A.05.07.11.004 The status code 0xFE MUST NOT be advertised after the transfer of an image for the Firmware ID
0 target (the “Z-Wave chip” image).



CC:007A.05.07.11.005



Controlling nodes implementing earlier versions of the Firmware Update Meta Data CC do not support
status codes defined for newer versions. Therefore, a device returning the Firmware Update Meta
Data Status Report Command MUST comply with the version implemented on the controlling device
(device sending the image). The device returning the Firmware Update Meta Data Status Report can
identify the version of the controlling device based on the Firmware Update Meta Data Request Get.
This may be done as follows:


 - If the Firmware Update Meta Data Request Get does not include Firmware Target and Fragment
Size (8 bytes), the controller is version 1 or 2


 - If the Firmware Update Meta Data Request Get includes Firmware Target and Fragment Size
but not Activation (11 bytes), the controller is version 3


 - If the Firmware Update Meta Data Request Get includes Activation but not Hardware Version
(12 bytes), the controller is version 4


 - If the Firmware Update Meta Data Request Get includes Hardware Version (13 bytes), the
controller is version 5.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 664




<!-- PAGE 666 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 3.71: Firmware Update Meta Data Status Report::Status
Encoding






















|Status|Description|Version|
|---|---|---|
|0x00|The device was unable to receive the requested frmware<br>data without checksum error.<br>Number of retries and request sequence of missing frames<br>are implementation specifc. The image is not stored.<br>|1|
|0x01|The device was unable to receive the requested frmware<br>data.<br>Number of retries and request sequence of missing frames<br>are implementation specifc. The image is not stored.|1|
|0x02|The transferred image does not match the Manufacturer<br>ID.<br>The image is not stored.|4|
|0x03|The transferred image does not match the Firmware ID.<br>The image is not stored.|4|
|0x04|The transferred image does not match the Firmware Tar-<br>get.<br>The image is not stored.<br>|4|
|0x05|Invalid fle header information.<br>The image is not stored.<br>|4|
|0x06|Invalid fle header format.<br>The image is not stored.<br>|4|
|0x07|Insufcient memory.<br>The image is not stored.|4|
|0x08|The transferred image does not match the Hardware ver-<br>sion.<br>The image is not stored.|5|
|…|_Reserved_|…|
|0xFD|Firmware image downloaded successfully, waiting for acti-<br>vation command.|4|
|0xFE|New<br>image<br>was<br>successfully<br>stored<br>in<br>temporary<br>non-volatile memory. The device does not restart itself.<br>This Status code MUST NOT be used when updating the<br>Z-Wave chip image|3|
|0xFF|New<br>image<br>was<br>successfully<br>stored<br>in<br>temporary<br>non-volatile memory and/or applied successfully. The sup-<br>porting node MAY restart itself. In this case, version 3 or<br>newer supporting nodes SHOULD use the WaitTime to<br>indicate that reboot has not been performed yet.|1|



CC:007A.05.07.11.006 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 665




<!-- PAGE 667 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.19.7** **Firmware** **Update** **Activation** **Set** **Command**


This command is used to initiate the programming of a previously transferred firmware image.


Refer to the Firmware Update Meta Data Status Report Command Status code 0xFD.


CC:007A.05.08.13.001 This command MAY be issued directly by a controlling node or MAY be scheduled for later execution
via the Schedule Command Class.


CC:007A.05.08.11.001 The Firmware Update Activation Status Report Command MUST be returned in response to this
command.


Table 3.72: Firmware Update Activation Set Command version 5

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|Command = FIRMWARE_UPDATE_ACTIVATION_SET|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|
|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|
|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|
|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|



All fields not described below remain unchanged from version 4.


**Firmware** **Checksum** **(16** **bits)**

CC:007A.05.08.11.002 The checksum field MUST carry the checksum of the firmware image about to be activated.


CC:007A.05.08.11.003 The checksum MUST be calculated using the CRC-CCITT polynomium using initialization value
equal to 0x1D0F and 0x1021 (normal representation).


For more details, refer to _CRC-CCITT_ _Source_ _Code_ .


**Hardware** **Version** **(8** **bits)**


Refer to Section 3.2.19.3 Firmware Meta Data Report Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 666




<!-- PAGE 668 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.19.8** **Firmware** **Update** **Activation** **Status** **Report** **Command**


This command is used to advertise the result of a firmware update operation initiated by the Firmware
Update Activation Set Command.


Table 3.73: Firmware Update Activation Status Report Command
version 5

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|
|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|
|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|
|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|
|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|



All fields not described below remain unchanged from version 4.


**Firmware** **Checksum** **(16** **bits)**

CC:007A.05.09.11.001 The checksum field MUST carry the checksum of the firmware image activated by the Firmware
Update Activation Set Command.


CC:007A.05.09.11.002 The checksum MUST be calculated using the CRC-CCITT polynomium using initialization value
equal to 0x1D0F and 0x1021 (normal representation).


For more details, refer to _CRC-CCITT_ _Source_ _Code_ .


**Hardware** **Version** **(8** **bits)**


Refer to Section 3.2.19.3 Firmware Meta Data Report Command.


**Firmware** **Update** **Status** **(8** **bits)**

CC:007A.05.09.11.003 The Firmware Update Status field MUST comply with Table 3.74.



Table 3.74: Firmware Update Activation Status Report::Firmware
Update Status Encoding









|Status|Description|Version|
|---|---|---|
|0x00|Invalid combination of manufacturer ID, frmware ID and<br>Hardware Version or Firmware Target. The received image<br>will not be stored.The device was unable to receive the<br>requested frmware data without checksum error.<br>|4|
|0x01|Error activating the frmware. Last known frmware image<br>has been restored.|4|
|…|_Reserved_|…|
|0xFF|Firmware update completed successfully.|4|


All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 667




<!-- PAGE 669 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.19.9** **Firmware** **Update** **Meta** **Data** **Prepare** **Get** **Command**


This command is used to request that a firmware download is initiated by the node sending this
command.


CC:007A.05.0A.11.001 The Firmware Update Meta Data Prepare Report Command MUST be returned in response to this
command when the receiving node is ready to send the requested firmware image.


CC:007A.05.0A.11.002 This command MUST NOT be issued via multicast addressing.


CC:007A.05.0A.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.



CC:007A.05.0A.12.001


CC:007A.05.0A.11.004



Any image transferred via the Firmware Update Meta Data Command Class SHOULD include a
fingerprint value to enable the validation of the integrity of the entire image after the transfer. The
image and the fingerprint value MUST be packed in one entity which can be stored in one file and
transferred as one entity.


Table 3.75: Firmware Update Meta Data Prepare Get Command

|7|Table 3.7 version 5 6|75: Firmware 5|e Update Me 4|eta Data Pre 3|epare Get C 2|Command 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_PREPARE_GET|Command = FIRMWARE_UPDATE_MD_PREPARE_GET|Command = FIRMWARE_UPDATE_MD_PREPARE_GET|Command = FIRMWARE_UPDATE_MD_PREPARE_GET|Command = FIRMWARE_UPDATE_MD_PREPARE_GET|Command = FIRMWARE_UPDATE_MD_PREPARE_GET|Command = FIRMWARE_UPDATE_MD_PREPARE_GET|Command = FIRMWARE_UPDATE_MD_PREPARE_GET|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|
|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|
|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|
|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|



Refer to Section 3.2.19.4 Firmware Update Meta Data Request Get Command for field description.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 668




<!-- PAGE 670 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.19.10** **Firmware** **Update** **Meta** **Data** **Prepare** **Report** **Command**


This command is used to advertise if the firmware image has been prepared and is ready to be
transferred.


Table 3.76: Firmware Update Meta Data Prepare Report Command version 5

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|
|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|



**Status** **(8** **bits)**

CC:007A.05.0B.11.001 The Status field MUST comply with Table 3.77.


Table 3.77: Firmware Update Meta Data Prepare Report::Status
encoding






|Status|Description|Version|
|---|---|---|
|0x00|ERROR. Invalid combination of Manufacturer ID and<br>Firmware ID.<br>The receiving node MUST NOT initiate the frmware<br>download.|5|
|0x01|ERROR. Device expected an authentication event to en-<br>able frmware update.<br>The receiving node MUST NOT initiate the frmware<br>download.|5|
|0x02|ERROR. The requested Fragment Size exceeds the Max<br>Fragment Size.<br>The receiving node MUST NOT initiate the frmware<br>download.<br>|5|
|0x03|ERROR. This frmware target is not downloadable.<br>The receiving node MUST NOT initiate the frmware<br>download.|5|
|0x04|ERROR. Invalid Hardware Version.<br>The receiving node MUST NOT initiate the frmware<br>download.<br>|5|
|0xFF|OK. The receiving node can initiate the frmware down-<br>load of the target specifed in the Firmware Update Meta<br>Data Prepare Get Command.|5|



CC:007A.05.0B.11.002 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Firmware** **Checksum** **(16** **bits)**

CC:007A.05.0B.11.003 The checksum field MUST carry the checksum of the firmware image about to be transferred.

CC:007A.05.0B.12.001 The checksum field value SHOULD be 0x00 if the Status field is set to a different value than 0xFF.


CC:007A.05.0B.11.004 The checksum MUST be calculated using the CRC-CCITT polynomium using initialization value
equal to 0x1D0F and 0x1021 (normal representation).


For more details, refer to _CRC-CCITT_ _Source_ _Code_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 669




<!-- PAGE 671 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.19.11** **Examples**


**3.2.19.11.1** **Identifying** **firmware** **revisions**


The different fields Manufacturer ID, Firmware ID and Hardware version are used to identify compatible firmware image with the product.


The Version Command Class is also used for identifying the Firmware version/subversion

An example of the different fields’ usage for a wall outlet is shown in Table 3.78.


Table 3.78: Labeling Different Firmware Revisions
















|Col1|i<br>Firmware Identifcation|Col3|Col4|Col5|
|---|---|---|---|---|
|Product|Manufac-<br>turer<br>ID|Hardware<br>Version|Firmware<br>ID|Firmware version/<br>subversion|
|Initial Wall Outlet|0x0001|0x01|0x0001|0x01/0x01|
|New Revision|New Revision|New Revision|New Revision|New Revision|
|Fix previous bugs|0x0001|0x01|0x0001|0x01/0x02|
|New revision|New revision|New revision|New revision|New revision|
|Introducing new features (e.g.<br>multiple press)|0x0001|0x01|0x0001|0x02/0x01|
|New revision|New revision|New revision|New revision|New revision|
|US version (initial version)|0x0001|0x01|0x0001|0x02/0x01|
|China version (matching local<br>requirements)|0x0001|0x01|0x0002|0x02/0x01|
|New revision|New revision|New revision|New revision|New revision|
|Proximity Sensor added (US)|0x0001|0x02|0x0001|0x02/0x01|
|Proximity Sensor added (China)|0x0001|0x02|0x0002|0x02/0x01|
|New revision|New revision|New revision|New revision|New revision|
|Adding S2 Capability (without<br>proximity sensor, US)|0x0001|0x01|0x0001|0x03/0x01|
|Adding S2 Capability (without<br>proximity sensor, China)|0x0001|0x01|0x0002|0x03/0x01|
|Adding S2 Capability (with<br>proximity sensor, US)|0x0001|0x02|0x0001|0x03/0x01|
|Adding S2 Capability (with<br>proximity sensor, China)|0x0001|0x02|0x0002|0x03/0x01|



An illustration of a controller retrieving the firmware information is given in Figure 3.5


Figure 3.5: Identifying Compatible Firmware Images


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 670




<!-- PAGE 672 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.19.11.2** **Firmware** **download**


The use of the Firmware Update Meta Data Prepare Get and Firmware Update Meta Data Prepare
Report commands is illustrated in Figure 3.6.


Figure 3.6: Firmware Download Flow Diagram


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 671

---

<!-- PAGE 673 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.20** **Firmware** **Update** **Meta** **Data** **Command** **Class,** **version** **6**


The Firmware Update Meta Data Command Class may be used to transfer a firmware image to or
from a Z-Wave node.


**3.2.20.1** **Compatibility** **considerations**


This version introduces new status codes for firmware update request responses in the Firmware
Meta Data Report Command and Firmware Update Meta Data Request Report Command. It also
allows a supporting node to advertise whether the application functionalities will be available during
a Firmware Update or not.


Firmware Update Meta Data Command Class, version 6 is backwards compatible with Firmware
Update Meta Data Command Class, version 5.

CC:007A.06.00.21.001 All commands and fields not mentioned in this version MUST remain unchanged from version 5.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 672




<!-- PAGE 674 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.20.2** **Firmware** **Meta** **Data** **Report** **Command**


This command is used to advertise the status of the current firmware in the device.


Table 3.79: Firmware Meta Data Report Command version 6

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|
|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|
|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|
|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|
|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|
|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|
|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|
|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|
|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|
|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|
|…|…|…|…|…|…|…|…|
|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|
|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|
|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|CC|



All fields not described below remain unchanged from version 5.


**CC** **(1** **bits)**

This field is used to advertise if the supporting node’s Command Classes functionality will continue
to function normally during Firmware Update transfer.

If all other Command Classes functionalities will function normally during firmware update image
CC:007A.06.03.11.001 transfer, this field MUST be set to 1.

If any Command Class functionality will not function normally during firmware update image transfer,
CC:007A.06.03.11.002 this field MUST be set to 0.

For example, if a node is unable to issue Notification Reports during firmware update, this field MUST
be set to 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 673




<!-- PAGE 675 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.20.3** **Firmware** **Update** **Meta** **Data** **Request** **Report** **Command**


This command is used to advertise if the firmware update will be initiated.


Table 3.80: Firmware Update Meta Data Request Report Command version 6

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT|
|Status|Status|Status|Status|Status|Status|Status|Status|



**Status** **(8** **bits)**

CC:007A.06.04.11.001 This field MUST comply with Table 3.81.


Table 3.81: Firmware Update Meta Data Request Report::Status
Encoding














|Status|Description|Version|
|---|---|---|
|0x00|ERROR. Invalid combination of Manufacturer ID and<br>Firmware ID.<br>The device will not initiate the frmware update.|1|
|0x01|ERROR. Device expected an authentication event to en-<br>able frmware update.<br>The device will not initiate the frmware update.|1|
|0x02|ERROR. The requested Fragment Size exceeds the Max<br>Fragment Size.<br>The device will not initiate the frmware update.<br>|3|
|0x03|ERROR. This frmware target is not upgradable.<br>The device will not initiate the frmware update.|3|
|0x04|ERROR. Invalid Hardware Version.<br>The device will not initiate the frmware update.<br>|5|
|0x05|ERROR: Another frmware image is current being trans-<br>ferred.<br>The device will not initiate the frmware update.<br>|6|
|0x06|ERROR: Insufcient battery level<br>The device will not initiate the frmware update.<br>|6|
|0xFF|OK. The device will initiate the frmware update of the<br>target specifed in the Firmware Update Meta Data Re-<br>quest Get Command.|1|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 674

---

<!-- PAGE 676 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.21** **Firmware** **Update** **Meta** **Data** **Command** **Class,** **version** **7**


The Firmware Update Meta Data Command Class may be used to transfer a firmware image to or
from a Z-Wave node.


**3.2.21.1** **Compatibility** **considerations**


This version introduces the ability to advertise if subsequent firmware activation is supported or not
by a node.


Firmware Update Meta Data Command Class, version 7 is backwards compatible with Firmware
Update Meta Data Command Class, version 6.

CC:007A.07.00.21.001 All commands and fields not mentioned in this version MUST remain unchanged from version 6.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 675




<!-- PAGE 677 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.21.2** **Firmware** **Meta** **Data** **Report** **Command**


This command is used to advertise the status of the current firmware in the device.


Table 3.82: Firmware Meta Data Report Command version 7

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|Command = FIRMWARE_MD_REPORT|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|
|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|
|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|
|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|
|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|
|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|
|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|
|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|
|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|
|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|
|…|…|…|…|…|…|…|…|
|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|
|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|
|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Activation|CC|



All fields not described below remain unchanged from version 6.


**Activation** **(1** **bits)**

This field is used to advertise if the supporting node supports subsequent activation after Firmware
Update transfer.

If the sending node supports the subsequent activation of firmware after downloading, this field MUST
be set to 1.

If the sending node does not support the subsequent activation of firmware after downloading, this
field MUST be set to 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 676




<!-- PAGE 678 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.21.3** **Firmware** **Update** **Meta** **Data** **Request** **Get** **Command**


Table 3.83: Firmware Meta Data Request Get Command version

|7|Table 3.8 7 6|83: Firmwar 5|re Meta Dat 4|ta Request G 3|Get Comman 2|nd version 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD|
|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|Command = FIRMWARE_UPDATE_MD_REQUEST_GET|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|
|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|
|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|
|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|
|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Activation|
|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|



All fields not described below remain unchanged from version 3.


**Activation** **(1** **bit)**

The Activation field is used to advertise if the receiving node must delay the actual firmware activation
after the file transfer.


A node advertising no support for “activation” in the Firmware Meta Data Report Command MUST
ignore this field and activate the Firmware immediately after download.


If the receiving node advertises support for Activation in the Firmware Meta Data Report Command:

 - The value ’1’ MUST indicate to delay the actual firmware update.

When delaying the firmware activation, the supporting node MUST set the Status code field to
0xFD in the Firmware Update Meta data Status Report Command.

 - The value ’0’ MUST indicate that the receiving device MUST NOT delay the firmware update
and activate the firmware immediately after download.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 677

---

<!-- PAGE 679 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.22** **Firmware** **Update** **Meta** **Data** **Command** **Class,** **version** **8**


The Firmware Update Meta Data Command Class may be used to transfer a firmware image to or
from a Z-Wave node.


**3.2.22.1** **Compatibility** **Considerations**


This version introduces the ability to perform firmware transfer without security encapsulation and
resume aborted firmware update attempts.


Firmware Update Meta Data Command Class, version 8 is backwards compatible with the Firmware
Update Meta Data Command Class, version 7.


**3.2.22.2** **Interoperability** **Considerations**


**3.2.22.2.1** **Interoperability** **with** **v1** **devices**


Version 2 of the _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ introduces a 16-bit Checksum field
to follow the variable-length Data field. No fields follow the variable-length Data field in Version 1
of the _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ . Subsequent versions of the Firmware Update
Meta Data Command Class command use the version 2 format.

At the same time, the specified method for determining the length of the variable-length Data field is
that the length must be calculated from the length of the received frame.


The unintended consequence is that a version 1 implementation receiving a _Firmware_ _Update_ _Meta_
_Data_ _Report_ _Command_ using version 2 format will consider the 16-bit Checksum field to be the last
two bytes of the Data field.


Similarly, a version 2 implementation receiving a _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_
version 1 will consider the last two bytes of the Data field to be the 16-bit Checksum field.


In either case, the transfer will fail.


Therefore, a node controlling the Firmware Update Meta Data Command Class, version 2 MUST do
CC:007A.08.00.31.001 the following when initiating the transfer of a firmware image:


1. Request the version of the Firmware Update Meta Data Command Class from the target device


2. Use the version of the _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ implemented by the
supporting node.

3. Determine the number of Data bytes that can fit into the _Firmware_ _Update_ _Meta_ _Data_ _Report_
_Command_ so that the complete command can still fit into the payload field of the transport
frame. The number of available payload bytes in the frame depends on the actual bit rate, the
use of security encapsulation as well as the presence of Checksum bytes in the _Firmware_ _Update_
_Meta_ _Data_ _Report_ _Command_ .


**3.2.22.2.2** **Checksum** **calculation**


Version 1 of the Firmware Update Meta Data Command Class introduced a 16-bit Checksum field used
to verify firmware image integrity. It has been a recommendation to use the CRC-CCITT polynomial
for calculating checksums. There is no way to identify what method has been used for calculating the
checksum for nodes implementing version 1 to version 4. Nodes having implemented another method
for calculating the checksum will find a non-matching checksum.


CC:007A.08.00.31.002 From Version 5 onwards, the checksum calculation method is mandatory. A version 5 supporting
node MUST calculate checksums using the CRC-CCITT polynomium using initialization value equal
to 0x1D0F and 0x1021 (normal representation). For more details about the checksum calculation,
refer to _CRC-CCITT_ _Source_ _Code_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 678




<!-- PAGE 680 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.22.2.3** **Firmware** **Activation**


CC:007A.08.00.31.003 Nodes supporting version 7 and newer MUST wait for a _Firmware_ _Update_ _Activation_ _Set_ _Command_
before activating a firmware after download, if instructed to use activation in the _Firmware_ _Update_
_Meta_ _Data_ _Request_ _Get_ _Command_ .


CC:007A.08.00.32.001 Nodes supporting version 6 or older are not mandated to so do. Controlling nodes SHOULD NOT
rely on the activation functionality for these versions.


**3.2.22.3** **Firmware** **Data** **fields**


Firmware are identified using the following fields:


**3.2.22.3.1** **Manufacturer** **ID** **(16** **bits)**


The Manufacturer ID is a unique ID identifying the manufacturer of the device. Manufacturer identifiers can be found in **Z-Wave** **Manufacturer** **ID** **List.xlsx** .

CC:007A.08.00.11.001 The first byte MUST be the most significant byte.


**3.2.22.3.2** **Firmware** **ID** **(16** **bits)**


Each firmware target has a Firmware ID. Firmware IDs may be identical for multiple targets.

CC:007A.08.00.11.002 The first byte MUST be the most significant byte.


**3.2.22.3.3** **Firmware** **Checksum** **(16** **bits)**


CC:007A.08.00.11.003 The checksum field MUST carry the checksum of the firmware image.


CC:007A.08.00.11.004 The checksum MUST be calculated using the CRC-CCITT polynomium using initialization value
equal to 0x1D0F and 0x1021 (normal representation).


For more details, refer to _CRC-CCITT_ _Source_ _Code_


**3.2.22.3.4** **Firmware** **target** **(8** **bits)**


This field MUST be used to identify the firmware image to be updated. The firmware images MUST
be identified according to Table 3.84.


Table 3.84: Firmware Update Meta Data Request Get Command
                       - Firmware Target encoding

|Firmware Target|Description|
|---|---|
|0 (0x00)|Firmware image targeted for the Z-Wave chip.<br>|
|1 (0x01)|Firmware image intended for target 1 defned by the manufacturer.|
|**…**|**…**<br>|
|255 (0xFF)|Firmware image intended for target 255 defned by the manufacturer.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 679




<!-- PAGE 681 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.22.3.5** **Hardware** **Version** **(8** **bits)**


CC:007A.08.00.11.005 This field MUST report a value which is unique to this particular version of the product.

CC:007A.08.00.11.006 It MUST be possible to uniquely identify applicable firmware images via the Manufacturer ID,
Firmware ID and the Hardware Version fields. This information allows selecting a firmware image
that is guaranteed to work with this particular version of the product.

CC:007A.08.00.11.007 The Hardware Version field MUST apply to the entire product and not only to the version of the
Z-Wave radio chip.

CC:007A.08.00.11.008 This field MUST report the same value as the Version CC Version Report Command: Hardware
Version field.


**3.2.22.4** **Firmware** **Meta** **Data** **Get** **Command**


This command is used to request firmware information and capabilities for a supporting node.


This command was introduced in version 1.


CC:007A.08.01.11.001 The _Firmware_ _Meta_ _Data_ _Report_ _Command_ MUST be returned in response to this command.


CC:007A.08.01.11.002 This command MUST NOT be issued via multicast addressing.


CC:007A.08.01.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.85: Firmware Meta Data Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|
|Command = FIRMWARE_MD_GET (0x01)|Command = FIRMWARE_MD_GET (0x01)|Command = FIRMWARE_MD_GET (0x01)|Command = FIRMWARE_MD_GET (0x01)|Command = FIRMWARE_MD_GET (0x01)|Command = FIRMWARE_MD_GET (0x01)|Command = FIRMWARE_MD_GET (0x01)|Command = FIRMWARE_MD_GET (0x01)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 680




<!-- PAGE 682 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.22.5** **Firmware** **Meta** **Data** **Report** **Command**


This command is used to advertise firmwares and capabilities of the supporting nodes.


This command was introduced in version 1.


Table 3.86: Firmware Meta Data Report Command



|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|
|Command = FIRMWARE_MD_REPORT (0x02)|Command = FIRMWARE_MD_REPORT (0x02)|Command = FIRMWARE_MD_REPORT (0x02)|Command = FIRMWARE_MD_REPORT (0x02)|Command = FIRMWARE_MD_REPORT (0x02)|Command = FIRMWARE_MD_REPORT (0x02)|Command = FIRMWARE_MD_REPORT (0x02)|Command = FIRMWARE_MD_REPORT (0x02)|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|Firmware 0 ID 1|
|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|Firmware 0 ID 2|
|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|Firmware 0 Checksum 1|
|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|Firmware 0 Checksum 2|
|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|Firmware Upgradable|
|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|Number of Firmware Targets|
|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|Max Fragment Size 1|
|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|Max Fragment Size 2|
|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|Firmware 1 ID 1|
|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|Firmware 1 ID 2|
|…|…|…|…|…|…|…|…|
|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|Firmware N ID 1|
|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|Firmware N ID 2|
|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|
|Reserved|Reserved|Reserved|Reserved|Resume|Non-secure|Activa-<br>tion|CC|


**Manufacturer** **ID** **(16** **bits)**


Refer to _Manufacturer_ _ID_ _(16_ _bits)_ .


**Firmware** **0** **ID** **(16** **bits)**

The Firmware 0 ID field is dedicated to target 0, i.e. the Z-Wave chip.





CC:007A.08.02.11.001 A manufacturer MUST assign a unique Firmware ID to each existing product variant. A product
variant may be a particular hardware version for a particular world region. The combination of Manufacturer ID and Firmware ID provides unique identification of a firmware image that is guaranteed
to work with a particular component of a particular product.

CC:007A.08.02.11.002 The first byte MUST be the most significant byte.

A user may request Manufacturer Specific information to get more detailed information on the product.

CC:007A.08.02.12.001 A controlling node SHOULD match the advertised firmware ID for the existing firmware image to
the firmware ID provided for a new image. If the firmware IDs do not match, the controlling device
SHOULD abort the firmware update operation.


**Firmware** **0** **Checksum** **(16** **bits)**

The checksum field is used to carry the checksum of the Firmware 0 Image.

CC:007A.08.02.13.001 Supporting nodes MAY set this field to 0x00. In this case the field is unused.


CC:007A.08.02.11.003 Values in the range 0x0001..0xFFFF indicate that the supporting node MUST advertise the checksum
of its firmware 0 image.


CC:007A.08.02.11.004 The checksum MUST be calculated using the CRC-CCITT polynomium using initialization value
equal to 0x1D0F and 0x1021 (normal representation).


For more details, refer to _CRC-CCITT_ _Source_ _Code_


**Firmware** **Upgradable** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 681




<!-- PAGE 683 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field defines whether the Z-Wave chip is firmware upgradable.

CC:007A.08.02.11.005 The value 0x00 MUST indicate that the firmware 0 image is not upgradable.

CC:007A.08.02.11.006 The value 0xFF MUST indicate that the firmware 0 image is upgradable.


**Number** **of** **Firmware** **Targets** **(8** **bits)**

CC:007A.08.02.11.007 The Number of Firmware Targets field MUST report the number of firmware IDs following this field.
The Firmware 0 ID field is not included. The field MUST be zero if the device only implements a
Firmware 0 target, i.e. the Z-Wave chip.


**Max** **Fragment** **Size** **(16** **bits)**

CC:007A.08.02.11.008 The Max Fragment Size field MUST report the maximum number of Data bytes that a device is able

CC:007A.08.02.13.002 to receive at a time. A sending node MAY send shorter fragments. The fragment size actually used is
indicated in the _Firmware_ _Update_ _Meta_ _Data_ _Request_ _Get_ _Command_ and confirmed in the _Firmware_
_Update_ _Meta_ _Data_ _Request_ _Report_ _Command_ .


The Max Fragment Size may be longer than the supported frame length of Z-Wave if the image is to
CC:007A.08.02.11.009 be transferred over e.g. IP. If the image is to be transferred over Z-Wave, the sending node MUST use
a fragment size which matches the actual number of available Data bytes. The number of available
Data bytes depends on the actual bit rate, the use of security encapsulation as well as the presence of
Checksum bytes in the Firmware Update Meta Data Report.


**Firmware** **1..N** **ID** **(16** **bits)**

The Firmware 1 ID field indicates the Firmware ID that MUST be used for target 1. The Firmware
2 ID field represents target 2. And so on.

CC:007A.08.02.11.00A The first byte MUST be the most significant byte.

CC:007A.08.02.12.002 A controlling device SHOULD match the advertised firmware ID for the existing firmware image to
the firmware ID provided for a new image. If the firmware IDs do not match, the controlling device
SHOULD abort the firmware update operation.


**Hardware** **Version** **(8** **bits)**


Refer to _Hardware_ _Version_ _(8_ _bits)_ .


**CC** **(1** **bit)**

This field is used to advertise if the supporting node’s Command Classes functionality will continue
to function normally during Firmware Update transfer.

CC:007A.08.02.11.00B If all other Command Classes functionalities will function normally during firmware update image
transfer, this field MUST be set to 1.


CC:007A.08.02.11.00C
If any Command Class functionality will not function normally during firmware update image transfer,
this field MUST be set to 0. For example, if a node is unable to issue Notification Reports during
firmware update, this field MUST be set to 0.


**Activation** **(1** **bit)**

This field is used to advertise if the supporting node supports subsequent activation after Firmware
Update transfer.


CC:007A.08.02.11.00D
If the sending node supports the subsequent activation of firmware after downloading, this field MUST
be set to 1.

CC:007A.08.02.11.00F If the sending node does not support the subsequent activation of firmware after downloading, this
field MUST be set to 0.


**Non-secure** **(1** **bit)**

This field is used to indicate if the node supports non-secure firmware transfers.


CC:007A.08.02.11.010 The value 0 MUST indicate that the non-secure transfer functionality is not supported.


CC:007A.08.02.11.011 The value 1 MUST indicate that the non-secure transfer functionality is supported.


**Resume** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 682




<!-- PAGE 684 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to indicate if the node supports resuming aborted firmware transfers.


CC:007A.08.02.11.012 The value 0 MUST indicate that the Resume functionality is not supported.


CC:007A.08.02.11.013 The value 1 MUST indicate that the Resume functionality is supported.


**3.2.22.6** **Firmware** **Update** **Meta** **Data** **Request** **Get** **Command**


The Firmware Update Meta Data Request Get Command is used to request that a firmware update
is initiated.


This command was introduced in version 1.


CC:007A.08.03.11.001 The _Firmware_ _Update_ _Meta_ _Data_ _Request_ _Report_ _Command_ MUST be returned in response to this
command.

CC:007A.08.03.11.002 The firmware update MUST NOT be initiated if the Manufacturer ID and the Firmware ID do not
match the actual firmware image values.


CC:007A.08.03.11.003
The firmware update MUST be aborted if the checksum does not match the calculated checksum after
the firmware image has been transferred.


CC:007A.08.03.11.004 This command MUST NOT be issued via multicast addressing.


CC:007A.08.03.11.005 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.87: Firmware Update Meta Data Request Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|
|Command = FIRMWARE_UPDATE_MD_REQUEST_GET (0x03)|Command = FIRMWARE_UPDATE_MD_REQUEST_GET (0x03)|Command = FIRMWARE_UPDATE_MD_REQUEST_GET (0x03)|Command = FIRMWARE_UPDATE_MD_REQUEST_GET (0x03)|Command = FIRMWARE_UPDATE_MD_REQUEST_GET (0x03)|Command = FIRMWARE_UPDATE_MD_REQUEST_GET (0x03)|Command = FIRMWARE_UPDATE_MD_REQUEST_GET (0x03)|Command = FIRMWARE_UPDATE_MD_REQUEST_GET (0x03)|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|
|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|
|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|
|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|
|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|
|Reserved|Reserved|Reserved|Reserved|Reserved|Resume|Non-secure|Activa-<br>tion|
|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|



**Manufacturer** **ID** **(16** **bits)**


Refer to _Manufacturer_ _ID_ _(16_ _bits)_ .


**Firmware** **ID** **(16** **bits)**

CC:007A.08.03.11.006 The Firmware ID MUST match the specified target of the actual device.


CC:007A.08.03.11.007
The firmware update MUST NOT be initiated if the Firmware ID does not match the specified target
of the actual device. The first byte MUST be the most significant byte.


**Firmware** **Checksum** **(16** **bits)**


Refer to _Firmware_ _Checksum_ _(16_ _bits)_ .


**Firmware** **Target** **(8** **bits)**


Refer to _Firmware_ _target_ _(8_ _bits)_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 683




<!-- PAGE 685 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Fragment** **Size** **(16** **bits)**

CC:007A.08.03.11.008 The Fragment Size field MUST report the fragment size that is to be used for firmware fragments.
A receiving device MUST use this fragment size for the firmware update. The fragment size is not
exchanged during the actual firmware update.



CC:007A.08.03.11.009


CC:007A.08.03.11.00A



The Fragment Size MUST NOT exceed the Max Fragment Size value of the _Firmware_ _Meta_ _Data_
_Report_ _Command_ . A version 1 _Firmware_ _Update_ _Meta_ _Data_ _Request_ _Get_ _Command_ does not carry a
Fragment Size field. A receiving node MUST determine the number of Data bytes from the length of
the first received frame, the use of security encapsulation as well as the presence of Checksum bytes
in the _Firmware_ _Meta_ _Data_ _Report_ _Command_ .


**Hardware** **Version** **(8** **bits)**


Refer to _Firmware_ _Meta_ _Data_ _Report_ _Command_ .


**Activation** **(1** **bit)**



CC:007A.08.03.11.014 The Activation field is used to advertise if the receiving node MUST delay the actual firmware activation after the file transfer.


CC:007A.08.03.11.00B A node advertising no support for “activation” in the _Firmware_ _Meta_ _Data_ _Report_ _Command_ MUST
ignore this field and activate the Firmware immediately after download.


If the receiving node advertises support for Activation in the _Firmware_ _Meta_ _Data_ _Report_ _Command_ :

CC:007A.08.03.11.00C - The value ’1’ MUST indicate to delay the actual firmware update. When delaying the firmware
activation, the supporting node MUST set the Status code field to 0xFD in the Firmware Update
Meta data Status Report Command.

CC:007A.08.03.11.00D - The value ’0’ MUST indicate that the receiving device MUST NOT delay the firmware update
and activate the firmware immediately after download.


**Resume** **(1** **bit)**

This field is used to request the supporting node to resume the firmware transfer from the last attempt.


CC:007A.08.03.11.00E Supporting nodes advertising no support for the Resume functionality in the _Firmware_ _Meta_ _Data_
_Report_ _Command_ MUST ignore this field and start the firmware update transfer from the Report
number 1.


CC:007A.08.03.11.00F The value 0 MUST indicate that the Firmware Update transfer MUST start from Report Number 1.


CC:007A.08.03.11.010 The value 1 MUST indicate that the Firmware Update transfer SHOULD start from The last received
report number in a previous transfer attempt for this firmware image.


**Non-Secure** **(1** **bit)**

This field is used to request the supporting node to accept receiving firmware fragments sent without
security encapsulation.


CC:007A.08.03.11.011 Supporting nodes advertising no support for the Non-Secure functionality in the _Firmware_ _Meta_
_Data_ _Report_ _Command_ MUST ignore this field and only accept _Firmware_ _Update_ _Meta_ _Data_ _Report_
_Command_ received at their highest granted security class.


CC:007A.08.03.11.012 The value 0 MUST indicate that the Firmware Update transfer MUST be performed securely and
the supporting node MUST only accept _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ received at
its highest granted security class.


CC:007A.08.03.11.013 The value 1 MUST indicate that the Firmware Update transfer SHOULD be done without security encapsulation and the supporting node SHOULD accept _Firmware Update Meta_ _Data Report Command_
received without security encapsulation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 684




<!-- PAGE 686 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.22.7** **Firmware** **Update** **Meta** **Data** **Request** **Report** **Command**


This command is used to advertise if the firmware update will be initiated.


This command was introduced in version 1.


Table 3.88: Firmware Update Meta Data Request Report Com
|7|Table 3. mand 6|.88: Firmwa 5|are Update M 4|Meta Data R 3|Request Repo 2|ort Com- 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|
|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT (0x04)|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT (0x04)|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT (0x04)|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT (0x04)|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT (0x04)|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT (0x04)|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT (0x04)|Command = FIRMWARE_UPDATE_MD_REQUEST_REPORT (0x04)|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Reserved|Reserved|Reserved|Reserved|Reserved|Resume|Non-secure|Reserved|



**Status** **(8** **bits)**

CC:007A.08.04.11.001 This field MUST comply with Table 3.89.




















|Status|Table 3.89: Firmware Update Meta Data Request Report Com- mand - Status encoding Description|Version|
|---|---|---|
|**Status**|**Description**|**Version**|
|0x00|_ERROR_. Invalid combination of Manufacturer ID and Firmware ID.<br>The device will not initiate the frmware update.<br>|1|
|0x01|_ERROR_. Device expected an authentication event to enable frmware<br>update.<br>The device will not initiate the frmware update.|1|
|0x02|_ERROR_. The requested Fragment Size exceeds the Max Fragment<br>Size.<br>The device will not initiate the frmware update.<br>|3|
|0x03|_ERROR_. This frmware target is not upgradable.<br>The device will not initiate the frmware update.|3|
|0x04|_ERROR_. Invalid Hardware Version.<br>The device will not initiate the frmware update.<br>|5|
|0x05|_ERROR_. Another frmware image is current being transferred.<br>The device will not initiate the frmware update.<br>|6|
|0x06|_ERROR_. Insufcient battery level.<br>The device will not initiate the frmware update.<br>|6|
|0xFF|_OK_. The device will initiate the frmware update of the target spec-<br>ifed in the _Firmware Update Meta Data Request Get Command_.|1|



CC:007A.08.04.11.002 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Resume** **(1** **bit)**

This field is used to indicate if the supporting node accepted to resume the firmware transfer from
the last attempt.


CC:007A.08.04.11.003 Supporting nodes advertising no support for the Resume functionality in the _Firmware_ _Meta_ _Data_
_Report_ _Command_ MUST set this field to 0 and start the firmware update transfer from the Report
number 1.


CC:007A.08.04.11.004 The value 0 MUST indicate that the supporting node did not (or cannot) accept to restart the previous
firmware update and it will start from Report Number 1.


CC:007A.08.04.11.005
The value 1 MUST indicate that the supporting node accepted to resume the previous firmware update
and it will start from the last received report number in a previous transfer attempt for this firmware
image.


**Non-Secure** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 685




<!-- PAGE 687 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to indicate if the supporting node accepted to receive firmware fragments sent
without security encapsulation.


CC:007A.08.04.11.006 Supporting nodes advertising no support for the Non-Secure functionality in the _Firmware_ _Meta_ _Data_
_Report_ _Command_ MUST set this field to 0 and and only accept _Firmware_ _Update_ _Meta_ _Data_ _Report_
_Command_ received at their highest granted security class.


CC:007A.08.04.11.007 The value 0 MUST indicate that the Firmware Update transfer will be performed securely and the
supporting node MUST only accept _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ received at its
highest granted security class.


CC:007A.08.04.11.008 The value 1 MUST indicate that the Firmware Update transfer will be performed without security
encapsulation and the supporting node MUST accept _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_
received without security encapsulation.


**3.2.22.8** **Firmware** **Update** **Meta** **Data** **Get** **Command**


This command is used to request one or more _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ .


This command was introduced in version 1.


CC:007A.08.05.11.001 The _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ MUST be returned in response to this command.



CC:007A.08.05.13.001


CC:007A.08.05.13.002



The transmission of the next _Firmware_ _Update_ _Meta_ _Data_ _Get_ _Command_ MAY be delayed if time is
required to store the most recent firmware fragment in temporary non-volatile memory. A node MAY
request multiple _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ to improve throughput.



CC:007A.08.05.11.002 This command MUST NOT be issued via multicast addressing.


CC:007A.08.05.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Two exceptions may apply: A noise burst may interfere the transmission or the data source may stop
returning _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ .


CC:007A.08.05.12.001 To accommodate for bursts of RF noise, a device receiving data SHOULD repeatedly retransmit the
same _Firmware_ _Update_ _Meta_ _Data_ _Get_ _Command_ every 10 seconds in case no _Firmware_ _Update_ _Meta_
_Data_ _Report_ _Command_ are received.


CC:007A.08.05.12.002 A device receiving data SHOULD stop retransmitting Firmware Update Meta Data Get Commands
and abort the ongoing firmare update 2 minutes after the last successful reception of a _Firmware_
_Update_ _Meta_ _Data_ _Report_ _Command_ .


Table 3.90: Firmware Update Meta Data Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|
|Command = FIRMWARE_UPDATE_MD_GET (0x05)|Command = FIRMWARE_UPDATE_MD_GET (0x05)|Command = FIRMWARE_UPDATE_MD_GET (0x05)|Command = FIRMWARE_UPDATE_MD_GET (0x05)|Command = FIRMWARE_UPDATE_MD_GET (0x05)|Command = FIRMWARE_UPDATE_MD_GET (0x05)|Command = FIRMWARE_UPDATE_MD_GET (0x05)|Command = FIRMWARE_UPDATE_MD_GET (0x05)|
|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|
|Res|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|
|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|



**Res** **(1** **bit)**

CC:007A.08.05.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Number** **of** **Reports** **(8** **bits)**


Number of _Firmware Update Meta Data Report Command_ to be received in response to this _Firmware_
_Update_ _Meta_ _Data_ _Get_ _Command_ .


**Report** **number** **(15** **bits)**

The Report number field indicates the _Firmware Update Meta Data Report Command_ to be requested.
CC:007A.08.05.11.005 The report number values MUST be a sequence starting from 1. The first byte (Report number 1) is
the most significant byte.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 686




<!-- PAGE 688 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.22.9** **Firmware** **Update** **Meta** **Data** **Report** **Command**


The Firmware Update Meta Data Report Command is used to transfer a firmware image fragment.


This command was introduced in version 1.


CC:007A.08.06.11.001 If sending more than a single _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ at a time, a node MUST
apply a delay between each transmitted command. The minimum required time delay and number of
frames before a delay must be inserted depends on the actual bit rate.


      - 40 kbit/s: At least 35 ms if sending more than 1 frame back-to-back


      - 100 kbit/s: At least 15 ms if sending more than 2 frames back-to-back


CC:007A.08.06.12.001 If needed, a controlling node SHOULD abort an ongoing transfer by responding to a _Firmware Update_
_Meta_ _Data_ _Get_ _Command_ with a _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ with the Last bit
enabled and the Data fields intentionally corrupted.

This will invalidate the calculated firmware checksum, which will eventually cause the receiving device
to return a _Firmware Update Meta Data Status Report Command_ with the status code 0x00 (checksum
error).


Table 3.91: Firmware Update Meta Data Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|
|Command = FIRMWARE_UPDATE_MD_REPORT (0x06)|Command = FIRMWARE_UPDATE_MD_REPORT (0x06)|Command = FIRMWARE_UPDATE_MD_REPORT (0x06)|Command = FIRMWARE_UPDATE_MD_REPORT (0x06)|Command = FIRMWARE_UPDATE_MD_REPORT (0x06)|Command = FIRMWARE_UPDATE_MD_REPORT (0x06)|Command = FIRMWARE_UPDATE_MD_REPORT (0x06)|Command = FIRMWARE_UPDATE_MD_REPORT (0x06)|
|Last|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|Report number 1|
|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|Report number 2|
|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|
|…|…|…|…|…|…|…|…|
|Data N|Data N|Data N|Data N|Data N|Data N|Data N|Data N|
|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|Checksum 1|
|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|Checksum 2|



**Last** **(1** **bit)**

This field indicates if this _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ is the last one.

CC:007A.08.06.11.002 The value 1 MUST indicate that this is the last report. Otherwise the field MUST be set to 0.


CC:007A.08.06.11.003 On the reception of the last image fragment, the receiving node MUST verify that the transferred
image does match the indicated Manufacturer ID, Firmware ID and Firmware Target values.


**Report** **number** **(15** **bits)**


CC:007A.08.06.11.004
The Report number field indicates the sequence number of the contained firmware fragment. The first
firmware fragment MUST be identified by the Report number value 1.

CC:007A.08.06.11.005 The sequence number of each following firmware fragment MUST be incremented. Report number 1
is the most significant byte.

The report number may be used to calculate the offset of the data by the formula:


_𝑂𝑓𝑓𝑠𝑒𝑡_ = ( _𝑅𝑒𝑝𝑜𝑟𝑡𝑁𝑢𝑚𝑏𝑒𝑟_ _−_ 1) _× 𝑁𝑢𝑚𝑏𝑒𝑟𝑜𝑓𝐷𝑎𝑡𝑎𝑓𝑖𝑒𝑙𝑑𝑠_ ( _𝑁_ )


CC:007A.08.06.11.006 Except for the last frame, each Report MUST carry the same number of Data bytes as the first
fragment. The last frame MAY carry a shorter Data field.


**Data** **(N** **bytes)**

The Data field is used to carry one firmware image fragment.


CC:007A.08.06.11.007 Except for the last frame, each _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ MUST carry the same
number of Data bytes as the first fragment. The last frame MAY carry a shorter Data field.


CC:007A.08.06.11.008


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 687




<!-- PAGE 689 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A sending device MUST use a fragment size which matches the actual number of available Data bytes.
The number of available Data bytes depends on the actual bit rate, the use of security encapsulation
as well as the presence of Checksum bytes in the Firmware Update Meta Data Report.

CC:007A.08.06.11.009 A receiving device MUST determine the number of Data bytes from the length of the first received
frame.


**Checksum** **(16** **bits)**

CC:007A.08.06.11.00A The checksum field MUST be used to ensure the consistency of the entire command; including the
command class and command identifiers.


CC:007A.08.06.11.00B The checksum MUST be calculated using the CRC-CCITT polynomium using initialization value
equal to 0x1D0F and 0x1021 (normal representation).


For more details, refer to _CRC-CCITT_ _Source_ _Code_

The Checksum field is known to cause compatibility issues with version 1 devices. Refer to Section
3.2.22.2.1 and Section 3.2.22.2.2


**3.2.22.10** **Firmware** **Update** **Meta** **Data** **Status** **Report** **Command**


This command is used to advertise the firmware update status.


This command was introduced in version 1.

CC:007A.08.07.11.001 The command MUST be issued when the firmware update is completed or aborted by the device
receiving the firmware.

CC:007A.08.07.12.001 A supporting node SHOULD reboot and apply the new firmware image before issuing this command.


CC:007A.08.07.11.002 A node MUST NOT issue Firmware Update Meta Data Get Command after receiving a Firmware
Update Meta Data Status Report.


Table 3.92: Firmware Update Meta Data Status Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|
|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT (0x07)|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT (0x07)|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT (0x07)|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT (0x07)|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT (0x07)|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT (0x07)|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT (0x07)|Command = FIRMWARE_UPDATE_MD_STATUS_REPORT (0x07)|
|Status|Status|Status|Status|Status|Status|Status|Status|
|WaitTime 1 (MSB)|WaitTime 1 (MSB)|WaitTime 1 (MSB)|WaitTime 1 (MSB)|WaitTime 1 (MSB)|WaitTime 1 (MSB)|WaitTime 1 (MSB)|WaitTime 1 (MSB)|
|WaitTime 2 (LSB)|WaitTime 2 (LSB)|WaitTime 2 (LSB)|WaitTime 2 (LSB)|WaitTime 2 (LSB)|WaitTime 2 (LSB)|WaitTime 2 (LSB)|WaitTime 2 (LSB)|



**Status** **(8** **bits)**

CC:007A.08.07.11.003 This field MUST comply with Table 3.93.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 688




<!-- PAGE 690 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024




















|Status|Table 3.93: Firmware Update Meta Data Status Report Command - Status encoding Description|Version|
|---|---|---|
|**Status**|**Description**<br>|**Version**|
|0x00|The device was unable to receive the requested frmware data without<br>checksum error. Number of retries and request sequence of missing<br>frames are implementation specifc. The image MAY be stored for<br>subsequent retries.<br>|1|
|0x01|The device was unable to receive the requested frmware data. Num-<br>ber of retries and request sequence of missing frames are implemen-<br>tation specifc. The image MAY be stored for subsequent retries.|1|
|0x02|The transferred image does not match the Manufacturer ID. The<br>image is not stored.|4|
|0x03|The transferred image does not match the Firmware ID. The image<br>is not stored.|4|
|0x04|The transferred image does not match the Firmware Target. The<br>image is not stored.<br>|4|
|0x05|Invalid fle header information. The image is not stored.<br>|4|
|0x06|Invalid fle header format. The image is not stored.<br>|4|
|0x07|Insufcient memory. The image is not stored.|4|
|0x08|The transferred image does not match the Hardware version The<br>image is not stored.|5|
|_0x09..0xFC_|_Reserved_|_N/A_|
|0xFD|Firmware image downloaded successfully, waiting for activation com-<br>mand.|4|
|0xFE|New image was successfully stored in temporary non-volatile mem-<br>ory.<br>The device does not restart itself.<br>This Status code MUST<br>NOT be used when updating the Z-Wave chip image|3|
|0xFF|New image was successfully stored in temporary non-volatile memory<br>and/or applied successfully. The supporting node MAY restart itself.<br>In this case, version 3 or newer supporting nodes SHOULD use the<br>WaitTime to indicate that reboot has not been performed yet.|1|



CC:007A.08.07.11.004 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**WaitTime** **(16** **bits)**

CC:007A.08.07.11.005 The WaitTime field MUST report the time that is needed before the receiving node again becomes
available for communication after the transfer of an image. The unit is the second.


CC:007A.08.07.11.006 The value 0 (zero) MUST indicate that the node is ready (it SHOULD have rebooted if needed and
applied the Firmware Image).


CC:007A.08.07.11.007 The value 0xFFFF is reserved and MUST NOT be returned.

CC:007A.08.07.12.002 A controlling node receiving this command SHOULD wait for the number of seconds specified in
this field before trying to resume communication. When resuming communication, the controlling
application SHOULD issue a NOP command and wait for acknowledgement.


CC:007A.08.07.12.003 The controlling application MAY attempt resuming communication repeatedly. In that case, the NOP
interval SHOULD be five seconds and MUST be at least one second.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 689




<!-- PAGE 691 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.22.11** **Firmware** **Update** **Activation** **Set** **Command**


This command is used to initiate the programming of a previously transferred firmware image.


This command was introduced in version 4.

Refer to the _Firmware_ _Update_ _Meta_ _Data_ _Status_ _Report_ _Command_ _Status_ field value 0xFD.


CC:007A.08.08.13.001 This command MAY be issued directly by a controlling node or MAY be scheduled for later execution
via the Schedule Command Class.


CC:007A.08.08.11.001 The _Firmware_ _Update_ _Activation_ _Status_ _Report_ _Command_ MUST be returned in response to this
command.


Table 3.94: Firmware Update Activation Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|
|Command = FIRMWARE_UPDATE_ACTIVATION_SET (0x08)|Command = FIRMWARE_UPDATE_ACTIVATION_SET (0x08)|Command = FIRMWARE_UPDATE_ACTIVATION_SET (0x08)|Command = FIRMWARE_UPDATE_ACTIVATION_SET (0x08)|Command = FIRMWARE_UPDATE_ACTIVATION_SET (0x08)|Command = FIRMWARE_UPDATE_ACTIVATION_SET (0x08)|Command = FIRMWARE_UPDATE_ACTIVATION_SET (0x08)|Command = FIRMWARE_UPDATE_ACTIVATION_SET (0x08)|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|
|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|
|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|
|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|



For fields’ description, refer to _Firmware_ _Data_ _fields_ .


**3.2.22.12** **Firmware** **Update** **Activation** **Status** **Report** **Command**


This command is used to advertise the result of a firmware update operation initiated by the _Firmware_
_Update_ _Activation_ _Set_ _Command_ .


This command was introduced in version 4.


Table 3.95: Firmware Update Activation Status Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|
|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT (0x09)|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT (0x09)|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT (0x09)|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT (0x09)|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT (0x09)|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT (0x09)|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT (0x09)|Command = FIRMWARE_UPDATE_ACTIVATION_STATUS_REPORT (0x09)|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|
|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|
|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|
|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|Firmware Update Status|
|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|



For fields not described below, refer to the _Firmware_ _Data_ _fields_ .


**Firmware** **Update** **Status** **(8** **bits)**

CC:007A.08.09.11.001 The Firmware Update Status field MUST comply with Table 3.96.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 690




<!-- PAGE 692 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 3.96: Firmware Update Activation Status Report Command
           - Firmware Update Status encoding









|Status|Description|Version|
|---|---|---|
|0x00|Invalid combination of manufacturer ID, frmware ID and Hardware<br>Version or Firmware Target. The received image will not be stored.<br>|4|
|0x01|Error activating the frmware. Last known frmware image has been<br>restored. The received image will not be stored.|4|
|_0x02..0xFE_|_Reserved_|_N/A_|
|0xFF|Firmware update completed successfully.|1|


CC:007A.08.09.11.002 Reserved values MUST NOT be used by a sending node and MUST be ignored by a receiving node.


**3.2.22.13** **Firmware** **Update** **Meta** **Data** **Prepare** **Get** **Command**


This command is used to request that a firmware download is initiated by the node sending this
command.

The purpose of this command is to download and backup the existing firmware from the device before
starting firmware upgrade.


This command was introduced in version 5.


CC:007A.08.0A.11.001 The _Firmware Update Meta Data Prepare Report Command_ Command MUST be returned in response
to this command when the receiving node is ready to send the requested firmware image or to advertise
that firmware is not downloadable.


CC:007A.08.0A.11.002 This command MUST NOT be issued via multicast addressing.


CC:007A.08.0A.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.



CC:007A.08.0A.12.001


CC:007A.08.0A.11.004



Any image transferred via the _Firmware_ _Update_ _Meta_ _Data_ _Command_ _Class,_ _version_ _8_ SHOULD
include a fingerprint value to enable the validation of the integrity of the entire image after the
transfer. The image and the fingerprint value MUST be packed in one entity which can be stored in
one file and transferred as one entity.


Table 3.97: Firmware Update Meta Data Prepare Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|
|Command = FIRMWARE_UPDATE_MD_PREPARE_GET (0x0A)|Command = FIRMWARE_UPDATE_MD_PREPARE_GET (0x0A)|Command = FIRMWARE_UPDATE_MD_PREPARE_GET (0x0A)|Command = FIRMWARE_UPDATE_MD_PREPARE_GET (0x0A)|Command = FIRMWARE_UPDATE_MD_PREPARE_GET (0x0A)|Command = FIRMWARE_UPDATE_MD_PREPARE_GET (0x0A)|Command = FIRMWARE_UPDATE_MD_PREPARE_GET (0x0A)|Command = FIRMWARE_UPDATE_MD_PREPARE_GET (0x0A)|
|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|Manufacturer ID 1|
|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|Manufacturer ID 2|
|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|Firmware ID 1|
|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|Firmware ID 2|
|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|Firmware Target|
|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|Fragment Size 1|
|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|Fragment Size 2|
|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|Hardware Version|



Refer to _Firmware_ _Data_ _fields_ for field description.


**Fragment** **Size** **(16** **bits)**



CC:007A.08.0A.11.005 The Fragment Size field MUST report the fragment size that is to be used for firmware fragments.
A receiving device MUST use this fragment size for the firmware update. The fragment size is not
exchanged during the actual firmware update.


CC:007A.08.0A.11.006 The Fragment Size MUST NOT exceed the Max Fragment Size value of the _Firmware_ _Meta_ _Data_
_Report_ _Command_ . A version 1 _Firmware_ _Update_ _Meta_ _Data_ _Request_ _Get_ _Command_ does not carry a
Fragment Size field. A receiving node MUST determine the number of Data bytes from the length of


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 691




<!-- PAGE 693 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


the first received frame, the use of security encapsulation as well as the presence of Checksum bytes
in the _Firmware_ _Meta_ _Data_ _Report_ _Command_ .


**3.2.22.14** **Firmware** **Update** **Meta** **Data** **Prepare** **Report** **Command**


This command is used to advertise if the firmware image has been prepared and is ready to be
transferred.


This command was introduced in version 5.


Table 3.98: Firmware Update Meta Data Prepare Report Com
|7|Table 3. mand 6|.98: Firmwar 5|re Update M 4|Meta Data Pr 3|repare Repor 2|rt Com- 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|Command Class = COMMAND_CLASS_FIRMWARE_UPDATE_MD (0x7A)|
|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT (0x0B)|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT (0x0B)|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT (0x0B)|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT (0x0B)|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT (0x0B)|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT (0x0B)|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT (0x0B)|Command = FIRMWARE_UPDATE_MD_PREPARE_REPORT (0x0B)|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|Firmware Checksum 1|
|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|Firmware Checksum 2|



**Status** **(8** **bits)**

CC:007A.08.0B.11.001 The Firmware Update Status field MUST comply with Table 3.99.











|Status|Table 3.99: Firmware Update Meta Data Prepare Report Com- mand - Status encoding Description|Version|
|---|---|---|
|**Status**|**Description**|**Version**|
|0x00|ERROR. Invalid combination of Manufacturer ID and Firmware ID.<br>The receiving node MUST NOT initiate the frmware download.<br>|5|
|0x01|ERROR. Device expected an authentication event to enable frmware<br>update. The receiving node MUST NOT initiate the frmware down-<br>load.|5|
|0x02|ERROR. The requested Fragment Size exceeds the Max Fragment<br>Size. The receiving node MUST NOT initiate the frmware down-<br>load.<br>|5|
|0x03|ERROR. This frmware target is not downloadable. The receiving<br>node MUST NOT initiate the frmware download.|5|
|0x04|ERROR. Invalid Hardware Version. The receiving node MUST NOT<br>initiate the frmware download.|5|
|_0x05..0xFE_|_Reserved_<br>|_N/A_|
|0xFF|OK. The receiving node can initiate the frmware download of the<br>target specifed in the _Firmware Update Meta Data Prepare Get_<br>_Command_.|5|


**Firmware** **Checksum** **(16** **bits)**


Refer to _Firmware_ _Checksum_ _(16_ _bits)_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 692




<!-- PAGE 694 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.22.15** **Firmware** **Update** **Examples** **and** **frame** **flows**


**3.2.22.15.1** **Requesting** **Firmware** **information**


Figure 3.7 shows a controlling node requesting the Firmware capabilities of another node by issuing
the _Firmware_ _Meta_ _Data_ _Get_ _Command_ .


Figure 3.7: Requesting firmware data from a node


**3.2.22.15.2** **Performing** **a** **Firmware** **update**


Figure 3.8 outlines the actual firmware update message flow. Prior to the firmware update, the
supporting node may receive an out-of-band authentication (e.g. physical activation of a pushbutton).


The controller sends a _Firmware Update Meta Data Request Get Command_ to initiate the downloading
a new firmware image.

The supporting node returns a _Firmware_ _Update_ _Meta_ _Data_ _Request_ _Report_ _Command_ to confirm the
update request and the supporting node begins pulling firmware image fragments from the controlling
node.


CC:007A.08.00.12.001 It is RECOMMENDED for controlling nodes to time out after a few minutes if no more _Firmware_
_Update_ _Meta_ _Data_ _Get_ _Command_ is received before the end of the transfer. In case of time out, the
controlling node SHOULD consider the firmware update as aborted/failed.


Finally a _Firmware_ _Update_ _Meta_ _Data_ _Status_ _Report_ _Command_ is returned to the controlling node to
indicate the success (or failure) of the update process.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 693




<!-- PAGE 695 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 3.8: Transferring a firmware image to a device


**3.2.22.15.3** **Identifying** **Firmware** **revisions**


The different fields Manufacturer ID, Firmware ID and Hardware version are used to identify compatible firmware image with the product. The _Version_ _Command_ _Class,_ _version_ _1_ _[OBSOLETED]_ is
also used for identifying the Firmware version/subversion An example of the different fields’ usage for
a wall outlet is shown in Table 3.100


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 694




<!-- PAGE 696 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 3.100: Labelling different Firmware revisions















|Product|i<br>Firmware identifcation|Col3|Col4|Col5|
|---|---|---|---|---|
|Product|Manufacturer<br>ID|Hardware<br>Version|Firmware<br>ID|Firmware<br>version/sub-version|
|Initial Wall outlet|0x0001|0x01|0x0001|0x01 / 0x01|
|New Revision|New Revision|New Revision|New Revision|New Revision|
|Fixing bugs|0x0001|0x01|0x0001|0x01 / 0x02|
|New Revision|New Revision|New Revision|New Revision|New Revision|
|New features|0x0001|0x01|0x0001|0x02 / 0x01|
|New Revision|New Revision|New Revision|New Revision|New Revision|
|US version (as before)|0x0001|0x01|0x0001|0x02 / 0x01|
|China version|0x0001|0x01|0x0002|0x02 / 0x01|
|New Revision|New Revision|New Revision|New Revision|New Revision|
|Hardware change (US)|0x0001|0x02|0x0001|0x02 / 0x01|
|Hardware change (China)|0x0001|0x02|0x0002|0x02 / 0x01|
|New Revision|New Revision|New Revision|New Revision|New Revision|
|Adding S2 (initial HW,<br>US)|0x0001|0x01|0x0001|0x03 / 0x01|
|Adding S2 (initial HW,<br>China)|0x0001|0x01|0x0002|0x03 / 0x01|
|Adding S2 (new HW, US)|0x0001|0x02|0x0001|0x03 / 0x01|
|Adding S2 (new HW,<br>China)|0x0001|0x02|0x0002|0x03 / 0x01|


An illustration of a controller retrieving the firmware information is given in Figure 3.9


Figure 3.9: Identifying compatible firmware images


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 695




<!-- PAGE 697 -->

CC:007A.08.00.12.002



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.22.15.4** **Firmware** **Activation**


A controlling node can instruct a supporting node to wait for activating its firmware after download.


**Note:** nodes supporting version 6 or older may not wait for the activation command after receiving
the _Firmware_ _Update_ _Meta_ _Data_ _Request_ _Get_ _Command_ with the _Activation_ field set to 1. It is
RECOMMENDED to use this functionality with nodes supporting version 7 or newer.


An example of a firmware activation is given in Figure 3.10.


Figure 3.10: Activating a firmware after transfer


**3.2.22.15.5** **Firmware** **download**


Some supporting nodes can allow to download their firmware for back-up reasons.


**Note:** Very few supporting nodes are capable of downloading their firmware.


Firmware downloads cannot be performed non-securely and cannot be resumed. An example of a
firmware download is given in Figure 3.11.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 696




<!-- PAGE 698 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 3.11: Downloading a firmware image from a node


**3.2.22.15.6** **Firmware** **Resume**


If a previous firmware update failed or was interrupted, the controlling and suppporting nodes can
agree on resuming the previous firmware update attempt.

CC:007A.08.00.12.003 The controlling node SHOULD request to resume firmware update if they actively decided to abort a
firmware update setting the _Last_ field to 1 in a _Firmware_ _Update_ _Meta_ _Data_ _Report_ _Command_ .

An example of resuming firmware update is shown in Figure 3.12


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 697




<!-- PAGE 699 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 3.12: Resuming a Firmware Update


CC:007A.08.00.12.004
A supporting node SHOULD accept to resume firmware transfer regardless of the Non-Secure setting,
i.e. resuming securely a non-secure transfer or vice-versa SHOULD be allowed.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 698




<!-- PAGE 700 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.22.15.7** **Non-secure** **Firmware** **update**


To increase the throughput of a firmware update, a controlling node and suppporting node can agree
on performing the Firmware Transfer without any Security encapsulation.

An illustration of a non-secure firmware update is shown in Figure 3.13


Figure 3.13: Performing a non-secure Firmware Update


**3.2.22.15.8** **Rejecting** **firmware** **updates** **or** **downloads**


Supporting nodes can reject firmware updates or downloads if they do not support the respective
functionality.

An illustration of a non-upgradable firmware is shown in Figure 3.14 and a non-downloadable firmware
is shown in Figure 3.15


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 699




<!-- PAGE 701 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 3.14: Rejecting a Firmware Update Request for non upgradable firmwares images


Figure 3.15: Rejecting a Firmware Download Request for non downloadable firmwares


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 700