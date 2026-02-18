<!-- PAGE 509 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.115** **Thermostat** **Setpoint** **Command** **Class,** **version** **3**


The Thermostat Setpoint Command Class is used to configure setpoints for the modes supported by
a thermostat.


**2.2.115.1** **Compatibility** **Considerations**


The Thermostat Setpoint Command Class, version 3 is backwards compatible with _Thermostat_ _Set-_
_point_ _Command_ _Class,_ _version_ _1-2_ .


This version introduces:


 - Setpoint capability discovery (allowed value range).


 - New setpoint types.


**2.2.115.2** **Interoperability** **Considerations**


It has been found that early implementations of this Command Class specification apply two
non-interoperable interpretations of the bit mask advertising the support for specific Setpoint Types.

As a consequence, one may find thermostat products and controller products in the marketplace which
implement either of the two bit mask interpretations found in Table 2.527. The notation x.y indicates
Bit Mask byte x, bit y.


Implementations of Thermostat Setpoint Command Class, version 3 MUST comply with Interpretation A.



Table 2.527: Thermostat Setpoint Types Bit Mask encoding















|Support Bit Mask<br>Interpretation A|Support Bit Mask<br>Interpretation B|Setpoint Type<br>i<br>Identifer|Description|Ver-<br>sion|
|---|---|---|---|---|
|1.0|1.0|0x00|N/A|-|
|1.1|1.1|0x01|Heating|1|
|1.2|1.2|0x02|Cooling|1|
||1.3|0x03|N/A|-|
||1.4|0x04|N/A|-|
||1.5|0x05|N/A|-|
||1.6|0x06|N/A|-|
|1.3|1.7|0x07|Furnace|1|
|1.4|2.0|0x08|Dry Air|1|
|1.5|2.1|0x09|Moist Air|1|
|1.6|2.2|0x0A|Auto<br>changeover|1|
|1.7|2.3|0x0B|Energy<br>Save<br>Heating|2|
|2.0|2.4|0x0C|Energy<br>Save<br>Cooling|2|
|2.1|2.5|0x0D|Away Heating|2|
|2.2|2.6|0x0E|Away Cooling|3|
|2.3|2.7|0x0F|Full Power|3|


All other bits are reserved and MUST be set to zero by a sending node. Reserved bits MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 508




<!-- PAGE 510 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.115.3** **Thermostat** **Setpoint** **Set** **Command**


This command is used to specify the target value for the specified Setpoint Type at a supporting
node.

A supporting node MUST support the same format of Precision, Scale and Size fields values as it
sends in the Thermostat Setpoint Supported Report Command or Thermostat Setpoint Capabilities
Report Command.

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

This field is used to specify the setpoint to be set at the receiving node.


The value MUST comply with Table 2.528.


Table 2.528: Thermostat Setpoint set::Setpoint Types

|Value|Description|CC Version|
|---|---|---|
|0x00|N/A|1|
|0x01|Heating|1|
|0x02|Cooling|1|
|0x03|N/A - reserved|-|
|0x04|N/A - reserved|-|
|0x05|N/A - reserved|-|
|0x06|N/A - reserved|-|
|0x07|Furnace|1|
|0x08|Dry Air|1|
|0x09|Moist Air|1|
|0x0A|Auto Changeover|1|
|0x0B|Energy Save Heating|2|
|0x0C|Energy Save Cooling|2|
|0x0D|Away Heating|2|
|0x0E|Away Cooling|3|
|0x0F|Full Power|3|



Values marked as not applicable (N/A) MUST be ignored by a receiving node. All other values are
reserved and MUST NOT be used by a sending node. Reserved values MUST be ignored by a receiving
node.


**Precision** **(3** **bits)**

This field is used to specify how many decimal places are included in the Value field. For example,
the decimal value 1025 with precision 2 MUST be interpreted as 10.25.


**Scale** **(2** **bits)**

This field is used to specify what temperature scale is used for the setpoint value.

The field MUST be encoded according to Table 2.529.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 509




<!-- PAGE 511 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.529: Thermostat Setpoint Set::Scale Encoding

|Value|i<br>Scale used in Value feld|
|---|---|
|0|Celsius|
|1|Fahrenheit|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Size** **(3** **bits)**

This field is used to indicate the length in bytes of the Value field.

This field MUST be set to 1, 2 or 4.


**Value** **(N** **bytes)**

This field is used to advertise the actual setpoint value to be set at the receiving node.

The length of this field MUST be according to the Size field value.

The first byte MUST be the most significant byte.

This field MUST be encoded using signed representation and comply with Table 2.12.


**2.2.115.4** **Thermostat** **Setpoint** **Get** **Command**


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


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 510




<!-- PAGE 512 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.115.5** **Thermostat** **Setpoint** **Report** **Command**


This command is used to advertise the value of a setpoint type.

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


The value MUST comply with Table 2.528.

If this field is set to 0x00 (N/A), it is RECOMMENDED to set the _Size_ field to 1 and the Value field
to 0.


**Precision** **(3** **bits)**

This field is used to indicate how many decimal places are included in the _Value_ field.

For example, the Value field set to 1025 with the _Precision_ field set to 2 MUST be interpreted as
10.25.


**Scale** **(2** **bits)**

This field is used to specify what temperature scale is used for the setpoint value.

The field MUST be encoded according to Table 2.529.


**Size** **(3** **bits)**

This field is used to indicate the length in bytes of the _Value_ field.

This field MUST be set to 1, 2 or 4.


**Value** **(N** **bytes)**

This field is used to advertise the actual setpoint value set at the sending node.

The length of this field MUST be according to the _Size_ field value.

The first byte MUST be the most significant byte.

This field MUST be encoded using signed representation and comply with Table 2.12.


A receiving node MUST ignore values outside the range advertised in the Thermostat Setpoint Capabilities Report Command for the actual Setpoint type.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 511




<!-- PAGE 513 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.115.6** **Thermostat** **Setpoint** **Supported** **Get** **Command**


This command is used to query the supported setpoint types.


The Thermostat Setpoint Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|
|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|Command = THERMOSTAT_SETPOINT_SUPPORTED_GET (0x04)|



**2.2.115.7** **Thermostat** **Setpoint** **Supported** **Report** **Command**


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


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 512




<!-- PAGE 514 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.115.8** **Thermostat** **Setpoint** **Capabilities** **Get** **Command**


This command is used request the supported setpoint value range for an actual Setpoint Type.


The Thermostat Setpoint Capabilities Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|
|Command = THERMOSTAT_SETPOINT_CAPABILITIES_GET (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_GET (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_GET (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_GET (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_GET (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_GET (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_GET (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_GET (0x09)|
|Reserved|Reserved|Reserved|Reserved|Setpoint Type|Setpoint Type|Setpoint Type|Setpoint Type|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Setpoint** **Type** **(4** **bits)**

This field is used to specify which setpoint is requested.


The value MUST comply with Table 2.528.


A supporting node receiving a supported Setpoint Type value MUST be return the same value in the
Thermostat Setpoint Capabilities Report Command.


A supporting node receiving a non-supported Setpoint Type value MUST return the value 0x00 (N/A)
in the Thermostat Setpoint Capabilities Report Command.


**2.2.115.9** **Thermostat** **Setpoint** **Capabilities** **Report** **Command**


This command is used advertise the supported setpoint value range for an actual Setpoint Type.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|Command Class = COMMAND_CLASS_THERMOSTAT_SETPOINT (0x43)|
|Command = THERMOSTAT_SETPOINT_CAPABILITIES_REPORT (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_REPORT (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_REPORT (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_REPORT (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_REPORT (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_REPORT (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_REPORT (0x09)|Command = THERMOSTAT_SETPOINT_CAPABILITIES_REPORT (0x09)|
|Reserved|Reserved|Reserved|Reserved|Setpoint Type|Setpoint Type|Setpoint Type|Setpoint Type|
|Min Value Precision|Min Value Precision|Min Value Precision|Min Value Scale|Min Value Scale|Min Value Size|Min Value Size|Min Value Size|
|Min Value 1|Min Value 1|Min Value 1|Min Value 1|Min Value 1|Min Value 1|Min Value 1|Min Value 1|
|…|…|…|…|…|…|…|…|
|Min Value N|Min Value N|Min Value N|Min Value N|Min Value N|Min Value N|Min Value N|Min Value N|
|Max Value Precision|Max Value Precision|Max Value Precision|Max Value Scale|Max Value Scale|Max Value Size|Max Value Size|Max Value Size|
|Max Value 1|Max Value 1|Max Value 1|Max Value 1|Max Value 1|Max Value 1|Max Value 1|Max Value 1|
|…|…|…|…|…|…|…|…|
|Max Value N|Max Value N|Max Value N|Max Value N|Max Value N|Max Value N|Max Value N|Max Value N|



**Setpoint** **Type** **(4** **bits)**

This field is used to advertise the setpoint advertised by the sending node.


The value MUST comply with Table 2.528.

If this field is set to 0x00 (N/A), it is RECOMMENDED to set the _Min_ _Value_ _Size_ and _Max_ _Value_
_Size_ fields to 1 and the _Min_ _Value_ and _Max_ _Value_ fields to 0.


**Min** **Value** **Precision** **(3** **bits)**

This field is used to indicate how many decimal places are included in the _Min_ _Value_ field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 513




<!-- PAGE 515 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


For example, the _Min_ _Value_ field set to 1025 with the _Min_ _Value_ _Precision_ field set to 2 MUST be
interpreted as 10.25.


**Min** **Value** **Scale** **(2** **bits)**

This field is used to specify what temperature scale is used for the setpoint _Min_ _Value_ field.

The field MUST be encoded according to Table 2.529.


**Min** **Value** **Size** **(3** **bits)**

This field is used to indicate the length in bytes of the _Min_ _Value_ field.

This field MUST be set to 1, 2 or 4.


**Min** **Value** **(N** **bytes)**

This field is used to advertise the minimum value that is supported for the actual setpoint at the
sending node.

The length of this field MUST be according to the _Min_ _Value_ _Size_ field value.

The first byte MUST be the most significant byte.

This field MUST be encoded using signed representation and comply with Table 2.12.


**Max** **Value** **Precision** **(3** **bits)**

This field is used to indicate how many decimal places are included in the _Max_ _Value_ field.

For example, the _Max_ _Value_ field set to 1025 with the _Max_ _Value_ _Precision_ field set to 2 MUST be
interpreted as 10.25.


**Max** **Value** **Scale** **(2** **bits)**

This field is used to specify what temperature scale is used for the setpoint _Max_ _Value_ field.

The field MUST be encoded according to Table 2.529 and this field MUST be set to the same value
as the _Min_ _Value_ _Scale_ field.


**Max** **Value** **Size** **(3** **bits)**

This field is used to indicate the length in bytes of the _Max_ _Value_ field.

This field MUST be set to 1, 2 or 4.


**Max** **Value** **(N** **bytes)**

This field is used to advertise the maximum value that is supported for the actual setpoint at the
sending node.

The length of this field MUST be according to the _Max_ _Value_ _Size_ field value.

The first byte MUST be the most significant byte.

This field MUST be encoded using signed representation and comply with Table 2.12.

This field MUST be set to a value greater than the _Min_ _Value_ field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 514