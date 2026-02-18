<!-- PAGE 98 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.11** **Authentication** **Media** **Write** **Command** **Class,** **version** **1** **[NEVER** **CERTIFIED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **NEVER** **BEEN** **CERTIFIED**

This command class has never been implemented and certified by a Z-Wave product Therefore,
this Command Class definition MAY be updated in a non-backwards compatible manner, or even
removed.


Consult with the Z-Wave Alliance Application Work Group if you consider implementing this
Command Class.


This command class is used to write raw Authentication Media data, such as RFID data contents on
tags.

The supported authentication medium itself is specific to individual nodes. Supporting nodes can use
the Entry Control Command Class to report the corresponding readings of their supported Authentication Media.


**2.2.11.1** **Authentication** **Media** **Capability** **Get** **Command**


This command is used to request the Authentication Media capabilities supported by the receiving
node.


The Authentication Media Capability Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.62: Authentication Media Capability Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|
|Command = AUTHENTICATION_MEDIA_CAPABILITIES_GET (0x01)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_GET (0x01)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_GET (0x01)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_GET (0x01)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_GET (0x01)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_GET (0x01)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_GET (0x01)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_GET (0x01)|



**2.2.11.2** **Authentication** **Media** **Capability** **Report** **Command**


This command is used to advertise the Authentication Media Command Class capabilities supported
by the sending node.


Table 2.63: Authentication Media Capability Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|
|Command = AUTHENTICATION_MEDIA_CAPABILITIES_REPORT (0x02)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_REPORT (0x02)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_REPORT (0x02)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_REPORT (0x02)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_REPORT (0x02)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_REPORT (0x02)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_REPORT (0x02)|Command = AUTHENTICATION_MEDIA_CAPABILITIES_REPORT (0x02)|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|DGS|



**DGS** **(Data** **Generation** **support)** **(1** **bit)**

This field is used to advertise if the supporting node has the capability to generate authentication
data that can be written on its authentication media.


This feature is used if the authentication media has a particular format and would not accept any
arbitral hexadecimal data.

If this field is set to 1, the supporting node MUST support creating authentication data for their write
operations.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 97




<!-- PAGE 99 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If this field is set to 0, the supporting node MUST NOT support creating authentication data for
their write operations.


**2.2.11.3** **Authentication** **Media** **Write** **Start** **Command**


This command is used to write Authentication Media contents (i.e., RFID data to a tag).


The Authentication Media Write Status Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.64: Authentication Media Write Start Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|
|Command = AUTHENTICATION_MEDIA_WRITE_START (0x03)|Command = AUTHENTICATION_MEDIA_WRITE_START (0x03)|Command = AUTHENTICATION_MEDIA_WRITE_START (0x03)|Command = AUTHENTICATION_MEDIA_WRITE_START (0x03)|Command = AUTHENTICATION_MEDIA_WRITE_START (0x03)|Command = AUTHENTICATION_MEDIA_WRITE_START (0x03)|Command = AUTHENTICATION_MEDIA_WRITE_START (0x03)|Command = AUTHENTICATION_MEDIA_WRITE_START (0x03)|
|Sequence number|Sequence number|Sequence number|Sequence number|Sequence number|Sequence number|Sequence number|Sequence number|
|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|
|Generate-<br>data|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Data Length|Data Length|Data Length|Data Length|Data Length|Data Length|Data Length|Data Length|
|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|
|…|…|…|…|…|…|…|…|
|Data N|Data N|Data N|Data N|Data N|Data N|Data N|Data N|



**Sequence** **number** **(8** **bits)**

This field is used to keep track of the Authentication Media Write Operation session.


A supporting node MUST return a Authentication Media Write Status Command with the status
field set to 0x03 if receiving this command with a different sequence number than the ongoing write
operation.


**Timeout** **(8** **bits)**

This field is used to specify how many seconds the receiving node MUST wait between the reception
of this command and aborting the write operation.


For nodes with a sensing/feeback capability for their authentication media write operation, this value
MUST also be used to wait that a media is accessible to the receiving node before the write operation
is aborted.


For Nodes without any feedback capability for their authentication media write operation MUST ignore this timeout value after and try to write the data on the authentication media target immediately.


**Generate** **data** **(1** **bit)**

This field is used to indicate the supporting node to generate the Authentication data that will be
written on the Authentication Media.

If this field is set to 1, the _Data_ _Length_ field MUST be set to 0.

If this field is set to 1, the supporting node MUST generate valid authentication data and return the
written data in the _Data_ field of the returned response.


**Data** **Length** **(8** **bits)**

This field is used to describe the length in bytes of the corresponding _Data_ field.

This field MUST be in the range 0..255.

This field MUST be set to a value higher than 0 if the _Generate_ _Data_ field is set to 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 98




<!-- PAGE 100 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Data** **(N** **bytes)**

This field is used to advertise the Data contents that MUST be written to the media.

The length of this field in bytes MUST be according to the corresponding _Data_ _Length_ field value.


**2.2.11.4** **Authentication** **Media** **Write** **Stop** **Command**


This command is used to interrupt an ongoing Authentication Media Write operation.


The Authentication Media Write Status Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.65: Authentication Media Write Stop Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|
|Command = AUTHENTICATION_MEDIA_WRITE_STOP (0x04)|Command = AUTHENTICATION_MEDIA_WRITE_STOP (0x04)|Command = AUTHENTICATION_MEDIA_WRITE_STOP (0x04)|Command = AUTHENTICATION_MEDIA_WRITE_STOP (0x04)|Command = AUTHENTICATION_MEDIA_WRITE_STOP (0x04)|Command = AUTHENTICATION_MEDIA_WRITE_STOP (0x04)|Command = AUTHENTICATION_MEDIA_WRITE_STOP (0x04)|Command = AUTHENTICATION_MEDIA_WRITE_STOP (0x04)|



**2.2.11.5** **Authentication** **Media** **Write** **Status** **Command**


This command is used to advertise the status of an Authentication Media Write operation.


Table 2.66: Authentication Media Write Status Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|Command Class = COMMAND_CLASS_AUTHENTICATION_MEDIA_WRITE (0xA2)|
|Command = AUTHENTICATION_MEDIA_WRITE_STATUS (0x05)|Command = AUTHENTICATION_MEDIA_WRITE_STATUS (0x05)|Command = AUTHENTICATION_MEDIA_WRITE_STATUS (0x05)|Command = AUTHENTICATION_MEDIA_WRITE_STATUS (0x05)|Command = AUTHENTICATION_MEDIA_WRITE_STATUS (0x05)|Command = AUTHENTICATION_MEDIA_WRITE_STATUS (0x05)|Command = AUTHENTICATION_MEDIA_WRITE_STATUS (0x05)|Command = AUTHENTICATION_MEDIA_WRITE_STATUS (0x05)|
|Sequence number|Sequence number|Sequence number|Sequence number|Sequence number|Sequence number|Sequence number|Sequence number|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Data Length|Data Length|Data Length|Data Length|Data Length|Data Length|Data Length|Data Length|
|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|
|…|…|…|…|…|…|…|…|
|Data N|Data N|Data N|Data N|Data N|Data N|Data N|Data N|



**Sequence** **number** **(8** **bits)**

This field is used to advertise the sequence number of the last Write operation.


If an Authentication Media Write Stop Command was received while no operation was ongoing, this
field SHOULD be set to 0x00.


**Data** **Length** **(8** **bits)**

This field is used to advertise the length in bytes of the _Data_ field.

This field MUST be in the range 0..255.

This field MUST be set to a value highest than 0 if the _Status_ field is set to 0xFE or 0xFF.


**Data** **(N** **bytes)**

This field is used to advertise the data that was written on the Authentication media as part of the
write operation.

This field MUST contain the data that was written on the media if the _Status_ field is set to 0xFE or
0xFF.


**Status** **(8** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 99




<!-- PAGE 101 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to indicate the status of the Authentication Media Write operation. This field MUST
encoded according to Table 2.67.

|Value|Table 2.67: Authentication Media Write Status::Status encoding Description|
|---|---|
|**Value**|**Description**|
|0x00|**Failed: Write operation not supported**<br>The node does not support write operations.|
|0x01|**Failed: Forced stop**<br>The node has received a Authentication Media Write Stop Command before the<br>data contents could be written on the target.|
|0x02|**Failed: timeout**<br>The node has timed out and could not write the data content on a target|
|0x03|**Failed: Another operation is ongoing**<br>The node has did not initiate the write operation as another operation was already<br>ongoing.|
|0x04|**Failed: Aborted**<br>The node has aborted the operation due to local input or other higherpriority task.<br>|
|0x05|**Failed: Bufer overfow**<br>The node could not start or aborted the write operation as it ran into a bufer<br>overfow while caching the data to write.|
|0x06|**Failed: Proprietary hex data restriction**<br>The node has received hexadecimal data that does not comply with the required<br>format for its Authentication Media data.<br>The controlling node should use the<br>“Generate-data” fag instead.<br>This status MUST NOT be returned by a node if it does not advertise support for<br>Data Generation in the Authentication Media Capability Report Command|
|0x07|**Failed: Non re-writable target**<br>The node could not write the data on the target as it already contains some data<br>that could not be overwritten.|
|0xFE|**Completed with no status:**<br>The Write Operation was carried out, but the node has no feedback from the media<br>writing operation and cannot confrm that the data was properly written on the<br>target.|
|0xFF|**Success**<br>The specifed data was properly written on the target.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 100