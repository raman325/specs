<!-- PAGE 503 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.113** **Thermostat** **Setback** **Command** **Class,** **version** **1**


The Thermostat Setback Command Class is used to change the current state of a non-schedule setback
thermostat.


**2.2.113.1** **Thermostat** **Setback** **Set** **Command**


This command is used to set the state of the thermostat.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|
|Command = THERMOSTAT_SETBACK_SET|Command = THERMOSTAT_SETBACK_SET|Command = THERMOSTAT_SETBACK_SET|Command = THERMOSTAT_SETBACK_SET|Command = THERMOSTAT_SETBACK_SET|Command = THERMOSTAT_SETBACK_SET|Command = THERMOSTAT_SETBACK_SET|Command = THERMOSTAT_SETBACK_SET|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Setback Type|Setback Type|
|Setback State|Setback State|Setback State|Setback State|Setback State|Setback State|Setback State|Setback State|



**Setback** **Type** **(2** **bits)**

The setback type field MUST comply with Table 2.525.


Table 2.525: Thermostat Setback Set::Setback Type encoding

|Value|Description|
|---|---|
|0x00|No override|
|0x01|Temporary override|
|0x02|Permanent override|
|0x03|Reserved|



**Note:** The temporary override provides an opportunity to implement a timer or equivalent in the
device. A temporary override will, if a timer is implemented, be terminated by the timer. If no timer
is implemented the temporary override MUST act as permanent override. If the temporary override
is implemented it MUST be documented in the user’s manual.


**Setback** **State** **(8** **bits)**


The Setback State MUST comply with Table 2.526.



Table 2.526: Thermostat Setback Set::Setback State encoding






|Setback State|Col2|Description|
|---|---|---|
|Hexadecimal|Decimal|Decimal|
|0x80<br>…<br>0xFF<br>0x00<br>0x01<br>…<br>0x78|-128<br>…<br>-1<br>0<br>1<br>…<br>120|The setback in 1/10 degrees (Kelvin)<br>Example:<br>0 = 0 degrees setback<br>1 = 0.1 degrees is added to the setpoint<br>2 = 0.2 degrees is added to the setpoint<br>-1 = 0.1 degrees is subtracted from the setpoint<br>-2 = 0.2 degrees is subtracted from the setpoint|
|0x79|121|Frost Protection|
|0x7A|122|Energy Saving Mode|
|0x7B-0x7E|123-126|Reserved|
|0x7F|127|Unused State|



Reserved values MUST NOT be used by a sending node. Reserved values MUST be ignored by a
receiving node.


When converting between Celsius and Fahrenheit proper rounding MUST be applied with at least
two decimals in the internal calculations of a device to avoid rounding errors.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 502




<!-- PAGE 504 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Note:** The implementation of Energy Saving Mode is manufacturer specific, and MUST be documented in the User’s Manual.


If the device is set to an unreachable state, the device SHOULD assume the closest possible state.


**2.2.113.2** **Thermostat** **Setback** **Get** **Command**


This command is used to request the current state of the thermostat.


The Thermostat Setback Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|
|Command = THERMOSTAT_SETBACK_GET|Command = THERMOSTAT_SETBACK_GET|Command = THERMOSTAT_SETBACK_GET|Command = THERMOSTAT_SETBACK_GET|Command = THERMOSTAT_SETBACK_GET|Command = THERMOSTAT_SETBACK_GET|Command = THERMOSTAT_SETBACK_GET|Command = THERMOSTAT_SETBACK_GET|



**2.2.113.3** **Thermostat** **Setback** **Report** **Command**


This command is used to report the current state of the thermostat.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|Command Class = COMMAND_CLASS_THERMOSTAT_SETBACK|
|Command = THERMOSTAT_SETBACK_REPORT|Command = THERMOSTAT_SETBACK_REPORT|Command = THERMOSTAT_SETBACK_REPORT|Command = THERMOSTAT_SETBACK_REPORT|Command = THERMOSTAT_SETBACK_REPORT|Command = THERMOSTAT_SETBACK_REPORT|Command = THERMOSTAT_SETBACK_REPORT|Command = THERMOSTAT_SETBACK_REPORT|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Setback Type|Setback Type|
|Setback State|Setback State|Setback State|Setback State|Setback State|Setback State|Setback State|Setback State|



**Setback** **Type** **(2** **bits)**


Refer to description under Thermostat Setback Set Command.


**Setback** **State** **(8** **bits)**


Refer to description under Thermostat Setback Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 503




<!-- PAGE 505 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.114** **Thermostat** **Setpoint** **Command** **Class,** **version** **1-2**


The Thermostat Setpoint Command Class is used to configure setpoints for the modes supported by
a thermostat.


**2.2.114.1** **Interoperability** **Considerations**


It has been found that early implementations of this Command Class specification apply two
non-interoperable interpretations of the bit mask advertising the support for specific Setpoint Types.

As a consequence, one may find thermostat products and controller products in the marketplace which
implement either of the two bit mask interpretations found in Table 2.527. The notation x.y indicates
Bit Mask byte x, bit y.


Implementations of Thermostat Setpoint Command Class, version 1-2 MUST comply with Interpretation A.


**2.2.114.2** **Thermostat** **Setpoint** **Set** **Command**


This command is used to specify the target value for the specified Setpoint Type at a supporting
node.

A supporting node MUST support the same format of Precision, Scale and Size fields values as it
sends in the Thermostat Setpoint Supported Report Command.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|
|Command = THERMOSTAT_SETPOINT_SET (0x01)|Command = THERMOSTAT_SETPOINT_SET (0x01)|Command = THERMOSTAT_SETPOINT_SET (0x01)|Command = THERMOSTAT_SETPOINT_SET (0x01)|Command = THERMOSTAT_SETPOINT_SET (0x01)|Command = THERMOSTAT_SETPOINT_SET (0x01)|Command = THERMOSTAT_SETPOINT_SET (0x01)|Command = THERMOSTAT_SETPOINT_SET (0x01)|
|Reserved|Reserved|Reserved|Reserved|Setpoint Type|Setpoint Type|Setpoint Type|Setpoint Type|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|
|…|…|…|…|…|…|…|…|
|Value N|Value N|Value N|Value N|Value N|Value N|Value N|Value N|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Setpoint** **Type** **(4** **bits)**

This field is used to specify the setpoint to be set at the receiving node .


The value MUST comply with Table 2.528.

If a non-supported setpoint type is specified, a receiving node MUST ignore the command.


**Precision** **(3** **bits)**

This field is used to indicate how many decimal places are included in the Value field.

For example, the Value field set to 1025 with the Precision field set to 2 MUST be interpreted as
10.25.


**Scale** **(2** **bits)**

This field is used to specify what temperature scale is used for the setpoint value.

The field MUST be encoded according to Table 2.529.


**Size** **(3** **bits)**

This field is used to indicate the length in bytes of the Value field.

This field MUST be set to 1, 2 or 4.


**Value** **(N** **bytes)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 504




<!-- PAGE 506 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to advertise the actual setpoint value to be set at the receiving node.

The length of this field MUST be according to the Size field value.

The first byte MUST be the most significant byte.

This field MUST be encoded using signed representation and comply with Table 2.12.


**2.2.114.3** **Thermostat** **Setpoint** **Get** **Command**


This command is used to request the target value for a given setpoint type that is currently configured
at a supporting node.


The Thermostat Setpoint Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|
|Command = THERMOSTAT_SETPOINT_GET (0x02)|Command = THERMOSTAT_SETPOINT_GET (0x02)|Command = THERMOSTAT_SETPOINT_GET (0x02)|Command = THERMOSTAT_SETPOINT_GET (0x02)|Command = THERMOSTAT_SETPOINT_GET (0x02)|Command = THERMOSTAT_SETPOINT_GET (0x02)|Command = THERMOSTAT_SETPOINT_GET (0x02)|Command = THERMOSTAT_SETPOINT_GET (0x02)|
|Reserved|Reserved|Reserved|Reserved|Setpoint Type|Setpoint Type|Setpoint Type|Setpoint Type|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Setpoint** **Type** **(4** **bits)**

This field is used to specify which setpoint is requested.


The value MUST comply with Table 2.528.


A supporting node receiving a supported Setpoint Type value MUST be return the same value in the
Thermostat Setpoint Report Command.


A supporting node receiving a non-supported Setpoint Type value MUST return the value 0x00 (N/A)
in the Thermostat Setpoint Report Command.


**2.2.114.4** **Thermostat** **Setpoint** **Report** **Command**


This command is used to advertise the target value for a given setpoint type that is currently configured
at the sending node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|
|Command = THERMOSTAT_SETPOINT_REPORT (0x03)|Command = THERMOSTAT_SETPOINT_REPORT (0x03)|Command = THERMOSTAT_SETPOINT_REPORT (0x03)|Command = THERMOSTAT_SETPOINT_REPORT (0x03)|Command = THERMOSTAT_SETPOINT_REPORT (0x03)|Command = THERMOSTAT_SETPOINT_REPORT (0x03)|Command = THERMOSTAT_SETPOINT_REPORT (0x03)|Command = THERMOSTAT_SETPOINT_REPORT (0x03)|
|Reserved|Reserved|Reserved|Reserved|Setpoint Type|Setpoint Type|Setpoint Type|Setpoint Type|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|
|…|…|…|…|…|…|…|…|
|Value N|Value N|Value N|Value N|Value N|Value N|Value N|Value N|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Setpoint** **Type** **(4** **bits)**

This field is used to advertise the setpoint advertised by the sending node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 505




<!-- PAGE 507 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value MUST comply with Table 2.528.

If this field is set to 0x00 (N/A), it is RECOMMENDED to set the Size field to 1 and the Value field
to 0.


**Precision** **(3** **bits)**

This field is used to indicate how many decimal places are included in the Value field.

For example, the Value field set to 1025 with the Precision field set to 2 MUST be interpreted as
10.25.


**Scale** **(2** **bits)**

This field is used to specify what temperature scale is used for the setpoint value.

The field MUST be encoded according to Table 2.529.


**Size** **(3** **bits)**

This field is used to indicate the length in bytes of the Value field.

This field MUST be set to 1, 2 or 4.


**Value** **(N** **bytes)**

This field is used to advertise the actual setpoint value set at the sending node.

The length of this field MUST be according to the Size field value.

The first byte MUST be the most significant byte.

This field MUST be encoded using signed representation and comply with Table 2.12.


**2.2.114.5** **Thermostat** **Setpoint** **Supported** **Get** **Command**


This command is used to query the supported setpoint types.


The Thermostat Setpoint Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|
|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|



**2.2.114.6** **Thermostat** **Setpoint** **Supported** **Report** **Command**


This command is used to advertise the supported setpoint types.


This command is known to cause interoperability issues. Refer to Section 2.2.114.1.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|
|Command = THERMOSTAT_SETPOINT_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_SETPOINT_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_SETPOINT_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_SETPOINT_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_SETPOINT_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_SETPOINT_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_SETPOINT_SUPPORTED_REPORT (0x05)|Command = THERMOSTAT_SETPOINT_SUPPORTED_REPORT (0x05)|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Bit** **Mask** **(N** **bytes)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 506




<!-- PAGE 508 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field advertises the supported Setpoint Types at the sending node.


A supporting node MUST support at least one setpoint type. Setpoint types and their minimum
required version are described in Table 2.528. A node MUST NOT support a setpoint type associated
to a newer version than the version it supports.

This field MUST be encoded according to Table 2.527, interpretation A:

 - Bit 0 in Bit Mask 1 represents Mode = 0x00 (Off).


 - Bit 1 in Bit Mask 1 represents Mode = 0x01 (Heat).


 - Bit 2 in Bit Mask 1 represents Mode = 0x02 (Cooling).


 - Bit 3 in Bit Mask 1 represents Mode = 0x07 (Furnace).


 - …


If a Setpoint Type is supported, the corresponding bit MUST be set to ‘1’.


If a Setpoint Type is not supported, the corresponding bit MUST be set to ‘0’.

This length of this field MUST be set to the minimum amount of bytes which allows advertising all
supported Setpoint Types.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 507