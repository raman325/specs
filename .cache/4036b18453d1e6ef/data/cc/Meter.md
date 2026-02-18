<!-- PAGE 282 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.55** **Meter** **Command** **Class,** **version** **1**


The Meter Command Class is used to advertise instantaneous and accumulated numerical readings.


The Command Class is intended for accumulated values in physical units from a water meter or
metering device (gas, electric etc.) and thereby enabling some automatic meter reading capabilities.


**2.2.55.1** **Terminology**


A meter is used to monitor a resource. The meter **accumulates** the resource flow over time. As an
option, the meter may report not only the most recent accumulated reading but also the previous
reading and the time that elapsed since then. A meter may also be able to report the current resource
flow. This is known as the **instant** value.


Meters may report two rate types. A utility installs **production** meters in its production facilities,
while it installs **consumption** meters at consumer premises. The difference is the mapping of the
physical flow direction to the **forward** **direction** of the meter:


 - The accumulated value of a production meter grows when more resources are produced


 - The accumulated value of a production meter drops when more resources are consumed


 - The accumulated value of a consumption meter grows when more resources are consumed


 - The accumulated value of a consumption meter drops when more resources are produced


If a meter only supports one rate type, the meter may **run** **backwards** . If a meter runs backwards,
the accumulated value may eventually become **negative** . While the production meter of a power
generator rarely runs backwards, the consumption meter in a private household with solar panels runs
backwards every time the solar panels deliver more than is consumed in the household. The actual
reading of a one-rate type meter reflects the net accumulated value since the meter was installed with
a factory default reading of zero. The accumulated value over an arbitrary interval may be calculated
by subtracting a previous accumulated value from the current accumulated value. Normal arithmetic
rules ensure that this also works in case of negative values.


A production meter may be used as a consumption meter by applying a sign change to all production
meter readings before using the values as consumption meter readings.


A meter device may advertise that it implements two separate registers for the production and consumption, respectively. In that case, both of these meters are always running forward: Production
makes the production meter run forward while consumption makes the consumption meter run forward. Two meter reports must be used to report the values of the respective meters.


**2.2.55.2** **Meter** **Get** **Command**


This command is used to request the current meter reading to a supporting node.


The Meter Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.338: Meter Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 281




<!-- PAGE 283 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.55.3** **Meter** **Report** **Command**


This command is used to advertise the current meter reading at the sending node.


This command MUST NOT be issued using broadcast addressing.


Table 2.339: Meter Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|
|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|
|…|…|…|…|…|…|…|…|
|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|



**Meter** **Type** **(8** **bits)**

This field is used to specify what type of metering physical unit is being reported.

This field MUST be encoded according to Table 2.358.


**Precision** **(3** **bits)**

This field MUST indicate how many decimal places are included in the Meter Value field. For example,
the _Meter_ _Value_ field set to 1025 and this field set to 2 MUST be interpreted as equal to 10.25.

The value of the precision field MUST be in the range 0..7.


**Scale** **(2** **bits)**

This field MUST advertise the unit used for the _Meter_ _Value_ field.

This field MUST be encoded according to Table 2.359.


**Size** **(3** **bits)**

This field indicates the length in bytes of the _Meter_ _Value_ field. This field MUST be set to 1, 2 or 4.


**Meter** **Value** **(N** **bytes)**

This field is used to advertise the actual meter reading.

The length of this field in bytes MUST be according to the _Size_ field.

The first byte MUST be the most significant byte.

This field MUST be encoded using signed representation and comply with Table 2.12.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 282

---

<!-- PAGE 284 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.56** **Meter** **Command** **Class,** **version** **2**


The Meter Command Class is used to advertise instantaneous and accumulated numerical readings.


The Command Class is intended for accumulated values in physical units from a water meter or
metering device (gas, electric etc.) and thereby enabling some automatic meter reading capabilities.


**2.2.56.1** **Compatibility** **Considerations**


The Meter Command Class, version 2 introduces the following functionalities:


 - Commands to interview supporting nodes Meter capabilities

 - New field ‘Previous Meter Value’ added to the Meter Report indicating consumption since
previous report.


 - An optional Meter Reset Command for resetting accumulated consumption.


 - New meter scales have been added

Commands and fields not mentioned in this version MUST remain unchanged from version 1.

Supporting nodes MAY support several scales. A manufacturer MUST define which scale is the default
scale and it MUST be described in the product manual.


**2.2.56.2** **Meter** **Supported** **Get** **Command**


This command is used to request the supported scales in a sub meter.


The Meter Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.340: Meter Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_SUPPORTED_GET (0x03)|Command = METER_SUPPORTED_GET (0x03)|Command = METER_SUPPORTED_GET (0x03)|Command = METER_SUPPORTED_GET (0x03)|Command = METER_SUPPORTED_GET (0x03)|Command = METER_SUPPORTED_GET (0x03)|Command = METER_SUPPORTED_GET (0x03)|Command = METER_SUPPORTED_GET (0x03)|



**2.2.56.3** **Meter** **Supported** **Report** **Command**


This command is used to advertise the supported scales and capabilities of the sending node.


Table 2.341: Meter Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|
|Meter Reset|Reserved|Reserved|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|
|Reserved|Reserved|Reserved|Reserved|Scale Supported|Scale Supported|Scale Supported|Scale Supported|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Meter** **Reset** **(1** **bit)**

This field is used to indicate if the sending node supports the Meter Reset Command.


The value 1 MUST indicate that the Meter Reset Command is supported.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 283




<!-- PAGE 285 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value 0 MUST indicate that the Meter Reset Command is not supported and MUST be ignored
by the sending node.


**Meter** **Type** **(5** **bits)**

This field is used to advertise the implemented meter type by the sending node.

This field MUST be encoded according to Table 2.358.


**Scale** **Supported** **(4** **bits)**

This field is used to advertise the supported scales of the sending node.


The bit value ‘1’ MUST indicate support for the actual scale.


The bit value ‘0’ MUST indicate that there is no support for the actual scale.

This MUST be interpreted as a bitmask in combination with the Meter Type field and MUST be
according to Table 2.356.


**2.2.56.4** **Meter** **Reset** **Command**


This command is used to reset all accumulated values stored at the receiving node.


Table 2.342: Meter Reset Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|



A supporting node MUST reset all its supported accumulated values when receiving this command if
it advertises support for Meter Reset in the Meter Supported Report Command.


A supporting node MUST ignore this command if it advertises no support for Meter Reset in the
Meter Supported Report Command


**2.2.56.5** **Meter** **Get** **Command**


This command is used to request the current meter reading to a supporting node .


The Meter Report Command MUST be returned in response to this command if the requested scale
is supported.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.343: Meter Get Command, version 2


**Reserved**

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|
|Reserved|Reserved|Reserved|Scale|Scale|Reserved|Reserved|Reserved|


This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Scale** **(2** **bits)**

This field is used to request an actual scale for the meter reading.

This field MUST be encoded according to Table 2.359.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 284




<!-- PAGE 286 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If this field is not present or set to 0x00, a supporting node MUST return a report using its default
scale.

A supporting node MUST ignored this command if this field is set to a non-supported scale.


For improved compatibility with version 1 controlling nodes, a supporting node receiving this command
without this field (version 1 format) SHOULD either return a version 1 Report Command or a Report
Command with the _Rate_ _Type_ field set to 0x00


**2.2.56.6** **Meter** **Report** **Command**


This command is used to advertise the current meter reading at the sending node.


This command MUST NOT be issued using broadcast addressing.


Table 2.344: Meter Report Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|
|Res|Rate Type|Rate Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|
|Precision|Precision|Precision|Scale|Scale|Size|Size|Size|
|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|
|…|…|…|…|…|…|…|…|
|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|
|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|
|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|
|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|
|…|…|…|…|…|…|…|…|
|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|



Fields not described below MUST remain unchanged from version 1.


**Res**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Rate** **Type** **(2** **bits)**

This field is used to indicate if the actual reading advertises import or export values.


The Import value for a meter reading MUST indicate that the reading represents a consumed amount.


The Export value for a meter reading MUST indicate that the reading represents a produced amount.

This field MUST be encoded according to Table 2.345.


Table 2.345: Meter Report::Rate Type encoding


**Meter** **Type** **(5** **bits)**

|Value|Rate Type|Version|
|---|---|---|
|0x00|Unspecifed|1|
|0x01|Import (consumed)|2|
|0x02|Export (produced)|2|
|0x03|Reserved|-|


This field is used to specify what type of metering physical unit is being reported.

This field MUST be encoded according to Table 2.358.


**Precision** **(3** **bits)**

This field MUST indicate how many decimal places are included in the _Meter_ _Value_ and _Previous_
_Meter_ _Value_ fields. For example, the _Meter_ _Value_ set to 1025 and this field set to 1 MUST be
interpreted as equal to 102.5.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 285




<!-- PAGE 287 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value of the precision field MUST be in the range 0..7.


**Scale** **(2** **bits)**

This field MUST advertise the unit used for the _Meter_ _Value_ and _Previous_ _Meter_ _Value_ fields.

This field MUST be encoded according to Table 2.359.


**Size** **(3** **bits)**

This field MUST indicate the length in bytes of the _Meter_ _Value_ and _Previous_ _Meter_ _Value_ fields.

This field MUST be set to 1, 2 or 4.


**Meter** **Value** **(N** **bytes)**

This field is used to advertise the actual meter reading.

The length of this field in bytes MUST be according to the _Size_ field.

The first byte MUST be the most significant byte.

The field MUST be encoded using signed representation and comply with Table 2.12.


**Delta** **Time** **(16** **bits)**

This field MUST advertise the elapsed time in seconds between the readings advertised by the _Meter_
_Value_ and the _Previous_ _Meter_ _Value_ fields. This field MUST be according to Table 2.346.


Table 2.346: Meter Report v2::Delta Time encoding

|Value|Description|
|---|---|
|0x0000|No Previous Meter Value feld is included in this command|
|0x0001..0xFFFE|1..65534 seconds have elapsed between reporting the Previous Meter Value<br>reading and the current meter reading|
|0xFFFF|Unknown elapsed time between the Previous Meter Value reading and the<br>current meter reading|



**Previous** **Meter** **Value** **(N** **bytes)**

This field is used to advertise the last issued meter reading for the actual scale.

This field MUST be omitted if the _Delta_ _Time_ field is set to the value 0.

The length of this field in bytes MUST be according to the _Size_ field if the _Delta_ _Time_ field is set to
a non-zero value.

The length of this field in bytes MUST be according to the _Size_ field.

The first byte MUST be the most significant byte.

The field MUST be encoded using signed representation and comply with Table 2.12.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 286

---

<!-- PAGE 288 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.57** **Meter** **Command** **Class,** **version** **3**


The Meter Command Class is used to advertise instantaneous and accumulated numerical readings.


The Command Class is intended for accumulated values in physical units from a water meter or
metering device (gas, electric etc.) and thereby enabling some automatic meter reading capabilities.


**2.2.57.1** **Compatibility** **Considerations**


The Meter Command Class, version 3 introduces the following functionalities:


 - New meter scales have been added.

Commands and fields not mentioned in this version MUST remain unchanged from version 2.

The manufacturer MUST define which scale is the default scale and it MUST be described in the
product manual.


The default scale MUST be in the range 0..3 as version 1 and version 2 controlling nodes will not be
able to interpret scale values in the range 4..7.


**2.2.57.2** **Meter** **Supported** **Report** **Command**


This command is used to advertise the supported scales and capabilities of the sending node.


Table 2.347: Meter Supported Report Command, version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|
|Meter Reset|Reserved|Reserved|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|
|Scale Supported|Scale Supported|Scale Supported|Scale Supported|Scale Supported|Scale Supported|Scale Supported|Scale Supported|



Fields not described below MUST remain unchanged from version 2.


**Scale** **Supported** **(8** **bits)**

This field is used to advertise the supported scales by the sending node.

The field MUST be treated as a bitmask in combination with the _Meter_ _Type_ field and MUST be
according to Table 2.356.


The bit value ‘1’ MUST indicate support for the actual scale.


The bit value ‘0’ MUST indicate that there is no support for the actual scale.


**2.2.57.3** **Meter** **Get** **Command**


This command is used to request the current meter reading to a supporting node.


The Meter Report Command MUST be returned in response to this command if the requested scale
is supported.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 287




<!-- PAGE 289 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.348: Meter Get Command, version 3


**Reserved**

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|
|Reserved|Reserved|Scale|Scale|Scale|Reserved|Reserved|Reserved|


This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Scale** **(3** **bits)**

This field is used to request an actual scale for the meter reading.

This field MUST be encoded according to Table 2.359.

If this field is not present or set to 0x00, a supporting node MUST return a report using its default
scale.

A supporting node MUST ignored this command if this field is set to a non-supported scale.


For improved compatibility with version 1 controlling nodes, a supporting node receiving this command
without this field (version 1 format) SHOULD either return a version 1 Report Command or a Report
Command with the _Rate_ _Type_ field set to 0x00


**2.2.57.4** **Meter** **Report** **command**


This command is used to advertise the current meter reading at the sending node.


This command MUST NOT be issued using broadcast addressing.


Table 2.349: Meter Report Command, version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|
|Scale (2)|Rate Type|Rate Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|
|Precision|Precision|Precision|Scale (1:0)|Scale (1:0)|Size|Size|Size|
|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|
|…|…|…|…|…|…|…|…|
|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|
|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|
|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|
|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|
|…|…|…|…|…|…|…|…|
|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|



Fields not described below MUST remain unchanged from version 2.


**Scale** **(3** **bits)**

This field MUST advertise the unit used for the _Meter_ _Value_ and _Previous_ _Meter_ _Value_ fields.

This field is composed of two sub-fields _Scale_ _(2)_ and _Scale_ _(1:0)_ which MUST be composed and
interpreted as one unit. _Scale_ _(2)_ MUST be the most significant bit.

This field MUST be encoded according to Table 2.359.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 288

---

<!-- PAGE 290 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.58** **Meter** **Command** **Class,** **version** **4**


The Meter Command Class is used to advertise instantaneous and accumulated numerical readings.


The Command Class is intended for accumulated values in physical units from a water meter or
metering device (gas, electric etc.) and thereby enabling some automatic meter reading capabilities.


**2.2.58.1** **Compatibility** **Considerations**


The Meter Command Class, version 4 introduces the following functionalities:


 - A supporting node can now support several rate types


 - New meter scales have been added

Commands and fields not mentioned in this version MUST remain unchanged from version 3.

The manufacturer MUST define which scale and rate types are the default and it MUST be described
in the product manual.


The default scale MUST be in the range 0..3 as version 1 and version 2 controlling nodes will not be
able to interpret scale values in the range 4..7.


**2.2.58.2** **Meter** **Supported** **Report** **Command**


This command is used to advertise the supported scales and capabilities of the sending node.


Table 2.350: Meter Supported Report Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|
|Meter Reset|Rate Type|Rate Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|
|M.S.T|Scale Supported “Byte 1”|Scale Supported “Byte 1”|Scale Supported “Byte 1”|Scale Supported “Byte 1”|Scale Supported “Byte 1”|Scale Supported “Byte 1”|Scale Supported “Byte 1”|
|Number of Scale Supported Bytes to Follow (optional)|Number of Scale Supported Bytes to Follow (optional)|Number of Scale Supported Bytes to Follow (optional)|Number of Scale Supported Bytes to Follow (optional)|Number of Scale Supported Bytes to Follow (optional)|Number of Scale Supported Bytes to Follow (optional)|Number of Scale Supported Bytes to Follow (optional)|Number of Scale Supported Bytes to Follow (optional)|
|Scale Supported “Byte 2” 1 (optional)|Scale Supported “Byte 2” 1 (optional)|Scale Supported “Byte 2” 1 (optional)|Scale Supported “Byte 2” 1 (optional)|Scale Supported “Byte 2” 1 (optional)|Scale Supported “Byte 2” 1 (optional)|Scale Supported “Byte 2” 1 (optional)|Scale Supported “Byte 2” 1 (optional)|
|…|…|…|…|…|…|…|…|
|Scale Supported “Byte N+1” N (optional)|Scale Supported “Byte N+1” N (optional)|Scale Supported “Byte N+1” N (optional)|Scale Supported “Byte N+1” N (optional)|Scale Supported “Byte N+1” N (optional)|Scale Supported “Byte N+1” N (optional)|Scale Supported “Byte N+1” N (optional)|Scale Supported “Byte N+1” N (optional)|



Fields not described below MUST remain unchanged from version 3.


**Rate** **Type** **(2** **bits)**

This field is used to indicate the supported rate types by the sending node.

This field MUST be encoded according to Table 2.351.

|Value|Table 2.351: Meter Supported Report::Rate Type encoding Supported rate types|Version|
|---|---|---|
|Value|Supported rate types|Version|
|0x00|Reserved|1..3|
|0x01|Import only (consumed)|4|
|0x02|Export only (produced)|4|
|0x03|Both Import and Export|4|



**Scale** **Supported** **“Byte** **1”** **(7** **bits)**

This field is used to advertise the supported scales by the sending node.

The field MUST be treated as a bitmask in combination with the _Meter_ _Type_ field and MUST be
according to Table 2.356.


The bit value ‘1’ MUST indicate support for the actual scale.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 289




<!-- PAGE 291 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The bit value ‘0’ MUST indicate that there is no support for the actual scale.


**M.S.T.** **(More** **Scale** **Types)** **(1** **bit)**

This field is used to indicate if the _Number_ _of_ _Scale_ _Supported_ _Bytes_ _to_ _Follow_ field is included in the
command.


The value 0 MUST indicate that the _Number_ _of_ _Scale_ _Supported_ _Bytes_ _to_ _Follow_ and subsequent
optional _Scale_ _Supported_ fields are omitted from the command.

The value 1 MUST indicate that the Number of _Scale_ _Supported_ _Bytes_ _to_ _Follow_ field is present in
the command.


**Number** **of** **Scale** **Supported** **to** **Follow** **(8** **bits)**

This field MUST indicate the length in bytes of the subsequent _Scale_ _Supported_ _(bytes_ _2..N+1)_ field.

This field MUST be omitted if the _M.S.T._ field is set to 0.


_Scale_ _Supported_ _(bytes_ _2..N+1)_ _(N_ _bytes)_

This field is used to advertise the supported scales by the sending node.

The length of this field in bytes MUST be according to the _Number of Scale Supported Bytes to Follow_
field.

This field MUST be omitted if the _M.S.T._ field is set to 0 or if the _Number_ _of_ _Scale_ _Supported_ _Bytes_
_to_ _Follow_ field is set to 0.

The field MUST be treated as a bitmask in combination with the _Meter_ _Type_ field and MUST be
according to Table 2.356.


The bit value ‘1’ MUST indicate support for the actual scale.


The bit value ‘0’ MUST indicate that there is no support for the actual scale.


**2.2.58.3** **Meter** **Get** **Command**


This command is used to request the current meter reading to a supporting node.


The Meter Report Command MUST be returned in response to this command if the requested scale
and rate type are supported.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.352: Meter Get Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|Command = METER_GET (0x01)|
|Rate Type|Rate Type|Scale|Scale|Scale|Reserved|Reserved|Reserved|
|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|



Fields not described below MUST remain unchanged from version 3.


**Rate** **Type** **(2** **bits)**

This field is used to request a rate type for the meter reading.

This field MUST be encoded according to Table 2.353.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 290




<!-- PAGE 292 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|Value|Table 2.353: Meter Get::Rate Type encoding Description|Version|
|---|---|---|
|Value|Description|Version|
|0x00|Default|1|
|0x01|Import (consumed)|4|
|0x02|Export (produced)|4|
|0x03|Reserved|-|



If supported, a receiving node MUST return a report for the requested Rate Type.

If this field is not present or set to 0x00, a receiving node MUST return a Report using its default
Rate Type.


**Scale** **(3** **bits)**

This field is used to request an actual scale for the meter reading.

This field MUST be encoded according to Table 2.359.

If this field is not present or set to 0x00, a supporting node MUST return a report using its default
scale.

A supporting node MUST ignored this command if this field is set to a non-supported scale.


For improved compatibility with version 1 controlling nodes, a supporting node receiving this command
without this field (version 1 format) SHOULD either return a version 1 Report Command or a Report
Command with the _Rate_ _Type_ field set to 0x00


The value 7 MUST indicate that the scale of the requested meter reading is advertised by the _Scale_
_2_ field.


**Scale** **2** **(8** **bits)**

This field is used to request an actual scale for the meter reading.

This field MUST be encoded according to Table 2.359.

This field MUST be present in the command if the _Scale_ field is set to 7 (M.S.T).

This field MUST be omitted if the _Scale_ field is set to a different value than 7.


**2.2.58.4** **Meter** **Report** **Command**


This command is used to advertise the current meter reading at the sending node.


This command MUST NOT be issued using broadcast addressing.


Table 2.354: Meter Report Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|
|Scale (2)|Rate Type|Rate Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|
|Precision|Precision|Precision|Scale (1:0)|Scale (1:0)|Size|Size|Size|
|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|
|…|…|…|…|…|…|…|…|
|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|
|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|
|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|
|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|
|…|…|…|…|…|…|…|…|
|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|
|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|



Fields not described below MUST remain unchanged from version 3.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 291




<!-- PAGE 293 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Scale** **(3** **bits)**

This field MUST advertise the unit used for the _Meter_ _Value_ and Previous* Meter Value fields.

This field is composed of two sub-fields _Scale_ _(2)_ and _Scale_ _(1:0)_ which MUST be composed and
interpreted as one unit. _Scale_ _(2)_ MUST be the most significant bit.

This field MUST be encoded according to Table 2.359.


The value 7 MUST indicate that the scale of the advertised meter reading is advertised by the _Scale_
_2_ field.


**Scale** **2** **(8** **bits)**

This field is used to advertise the unit used for the _Meter_ _Value_ and _Previous_ _Meter_ _Value_ fields.

This field MUST be present in the command if the _Scale_ field is set to 7 (M.S.T).

This field MUST be omitted if the _Scale_ field is set to a different value than 7.

This field MUST be encoded according to Table 2.359


Reserved values MUST NOT be used by a sending node. Reserved values MUST be ignored by a
receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 292

---

<!-- PAGE 294 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.59** **Meter** **Command** **Class,** **version** **5**


The Meter Command Class is used to advertise instantaneous and accumulated numerical readings.


The Command Class is intended for accumulated values in physical units from a water meter or
metering device (gas, electric etc.) and thereby enabling some automatic meter reading capabilities.


**2.2.59.1** **Compatibility** **considerations**


The Meter Command Class, version 5 adds support for Heating and Cooling Meter types.


The Meter Command Class, version 5 is backwards compatible with version 4.

Commands and fields not described in this version MUST remain unchanged from version 4.


**2.2.59.2** **Meter** **Supported** **Report** **Command**


This command is used to advertise supported scales and capabilities of the sending.


Table 2.355: Meter Supported Report Command, version 5

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|Command = METER_SUPPORTED_REPORT (0x04)|
|Meter Reset|Rate Type|Rate Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|
|M.S.T|Scale Supported “Byte 1”|Scale Supported “Byte 1”|Scale Supported “Byte 1”|Scale Supported “Byte 1”|Scale Supported “Byte 1”|Scale Supported “Byte 1”|Scale Supported “Byte 1”|
|Number of Scale Supported Bytes to Follow (Version 4 Extension)|Number of Scale Supported Bytes to Follow (Version 4 Extension)|Number of Scale Supported Bytes to Follow (Version 4 Extension)|Number of Scale Supported Bytes to Follow (Version 4 Extension)|Number of Scale Supported Bytes to Follow (Version 4 Extension)|Number of Scale Supported Bytes to Follow (Version 4 Extension)|Number of Scale Supported Bytes to Follow (Version 4 Extension)|Number of Scale Supported Bytes to Follow (Version 4 Extension)|
|Scale Supported 1 “Byte 2”|Scale Supported 1 “Byte 2”|Scale Supported 1 “Byte 2”|Scale Supported 1 “Byte 2”|Scale Supported 1 “Byte 2”|Scale Supported 1 “Byte 2”|Scale Supported 1 “Byte 2”|Scale Supported 1 “Byte 2”|
|…|…|…|…|…|…|…|…|
|Scale Supported N “Byte N+1”|Scale Supported N “Byte N+1”|Scale Supported N “Byte N+1”|Scale Supported N “Byte N+1”|Scale Supported N “Byte N+1”|Scale Supported N “Byte N+1”|Scale Supported N “Byte N+1”|Scale Supported N “Byte N+1”|



All fields not described below MUST remain unchanged from version 4.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 293




<!-- PAGE 295 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 2.356: Meter Supported Report::Scale Supported Bitmask
encoding


































|Meter<br>Type|Scale|Scale Supported Byte<br>Number|Scale Supported Bit<br>position|Measurement<br>mode|Ver-<br>sion|
|---|---|---|---|---|---|
|Electric<br>Meter|kWh|Byte 1|Bit 0|Accumulated|1|
|Electric<br>Meter|kVAh|Byte 1|Bit 1|Accumulated|2|
|Electric<br>Meter|W|Byte 1|Bit 2|Instant|2|
|Electric<br>Meter|Pulse<br>count|Byte 1|Bit 3|Accumulated|2|
|Electric<br>Meter|V|Byte 1|Bit 4|Instant|3|
|Electric<br>Meter|A|Byte 1|Bit 5|Instant|3|
|Electric<br>Meter|Power<br>factor|Byte 1|Bit 6|Instant|3|
|Electric<br>Meter|kVar|Byte 2|Bit 0|Instant|4|
|Electric<br>Meter|kVarh|Byte 2|Bit 1|Accumulated|4|
|Electric<br>Meter|Reserved|Byte 2|Bit 2-7|Reserved|-|
|Gas me-<br>ter|Cubic<br>meters|Byte 1|Bit 0|Accumulated|1|
|Gas me-<br>ter|Cubic<br>feet|Byte 1|Bit 1|Accumulated|2|
|Gas me-<br>ter|Reserved|Byte 1|Bit 2|n/a|-|
|Gas me-<br>ter|Pulse<br>count|Byte 1|Bit 3|Accumulated|2|
|Gas me-<br>ter|Reserved|Byte 1|Bit 4-6|Reserved|-|
|Gas me-<br>ter|Reserved|Byte 2|Bit 0-7|Reserved|-|
|Water<br>meter|Cubic<br>meters|Byte 1|Bit 0|Accumulated|1|
|Water<br>meter|Cubic<br>feet|Byte 1|Bit 1|Accumulated|1|
|Water<br>meter|US<br>gallons|Byte 1|Bit 2|Accumulated|1|
|Water<br>meter|Pulse<br>count|Byte 1|Bit 3|Accumulated|2|
|Water<br>meter|Reserved|Byte 1|Bit 4-6|Reserved|-|
|Water<br>meter|Reserved|Byte 2|Bit 0-7|Reserved|-|
|Heating<br>meter|kWh|Byte 1|Bit 0|Accumulated|5|
|Heating<br>meter|Reserved|Byte 1|Bit 1-6|Reserved|-|
|Heating<br>meter|Reserved|Byte 2|Bit 0-7|Reserved|-|
|Cooling|kWh|Byte 1|Bit 0|Accumulated|5|
|Cooling|Reserved|Byte 1|Bit 1-6|Reserved|-|
|Cooling|Reserved|Byte 2|Bit 0-7|Reserved|-|



**2.2.59.3** **Meter** **Report** **Command**


This command is used to advertise the current meter reading at the sending node.


This command MUST NOT be issued using broadcast addressing.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 294




<!-- PAGE 296 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.357: Meter Report Command, version 5

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|Command = METER_REPORT (0x02)|
|Scale (2)|Rate Type|Rate Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|
|Precision|Precision|Precision|Scale (1:0)|Scale (1:0)|Size|Size|Size|
|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|
|…|…|…|…|…|…|…|…|
|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|
|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|Delta Time 1|
|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|Delta Time 2|
|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|Previous Meter Value 1 (optional)|
|…|…|…|…|…|…|…|…|
|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|Previous Meter Value N (optional)|
|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|



Fields not described below MUST remain unchanged from version 4.


**Meter** **Type** **(5** **bits)**

This field is used to specify what type of metering physical unit is being reported.

This field MUST be encoded according to Table 2.358.

|Value|Table 2.358: Meter Report::Meter Type encoding Meter Type|Version|
|---|---|---|
|Value|Meter Type|Version|
|0x01|Electric meter|1|
|0x02|Gas meter|1|
|0x03|Water meter|1|
|0x04|Heating meter|5|
|0x05|Cooling meter|5|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Scale** **(3** **bits)**

This field MUST advertise the unit used for the _Meter_ _Value_ and _Previous_ _Meter_ _Value_ fields . This
field is composed of two sub-fields _Scale (2)_ and _Scale (1:0)_, which MUST be composed and interpreted
as one unit. _Scale_ _(2)_ MUST be the most significant bit.

This field MUST be encoded according to Table 2.359.


The value 0x07 MUST indicate that the scale of the advertised meter reading is advertised through
the _Scale_ _2_ field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 295




<!-- PAGE 297 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.359: Meter Report::Scale / Scale 2 encoding

|Meter Type|Scale (0:2) Value|Scale 2 Value|Unit|Version|
|---|---|---|---|---|
|Electric meter|0x00|0x00 (See Scale 0:2)|kWh|1|
|Electric meter|0x01|0x01|kVAh|2|
|Electric meter|0x02|0x02|W|2|
|Electric meter|0x03|0x03|Pulse count|2|
|Electric meter|0x04|0x04|V|3|
|Electric meter|0x05|0x05|A|3|
|Electric meter|0x06|0x06|Power Factor|3|
|Electric meter|0x07 (See Scale 2)|0x00|kVar|4|
|Electric meter|0x07 (See Scale 2)|0x01|kVarh|4|
|Gas meter|0x00|0x00 (See Scale 0:2)|Cubic meters|1|
|Gas meter|0x01|0x01|Cubic feet|2|
|Gas meter|0x02|0x02|Reserved|-|
|Gas meter|0x03|0x03|Pulse count|2|
|Gas meter|0x04..0x06|0x04..0x06|Reserved|-|
|Water meter|0x00|0x00 (See Scale 0:2)|Cubic meters|1|
|Water meter|0x01|0x01|Cubic feet|1|
|Water meter|0x02|0x02|US Gallons|1|
|Water meter|0x03|0x03|Pulse count|2|
|Water meter|0x04..0x06|0x04..0x06|Reserved|-|
|Heating meter|0x00|0x00 (See Scale 0:2)|kWh|5|
|Cooling meter|0x00|0x00 (See Scale 0:2)|kWh|5|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 296

---

<!-- PAGE 298 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.60** **Meter** **Command** **Class,** **version** **6**


The Meter Command Class is used to advertise instantaneous and accumulated numerical readings.


The Command Class is intended for accumulated values in physical units from a water meter or
metering device (gas, electric etc.) and thereby enabling some automatic meter reading capabilities.


**2.2.60.1** **Compatibility** **Considerations**


The Meter Command Class, version 6 adds a functionality to reset the accumulated value stored at
receiving node to specific.values.


The Meter Command Class, version 6 is backwards compatible with version 5.

Commands and fields not described in this version MUST remain unchanged from version 5.


**2.2.60.2** **Meter** **Reset** **Command**


This command is used to reset the accumulated values stored at the receiving node.


If the node advertises support for Meter Reset in the Meter Supported Report Command, the supporting node MUST reset the accumulated values to specific values, instead of setting to zero, when
receiving this command.


A supporting node MUST ignore this command if it advertises no support for Meter Reset in the
Meter Supported Report Command.


A supporting node MUST ignore this command if it receives it for a non-supported Meter Type, Rate
Type or Scale combination.


Table 2.360: Meter Reset Command, version 6

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|Command Class = COMMAND_CLASS_METER|
|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|Command = METER_RESET (0x05)|
|Scale (2)|Rate Type|Rate Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|
|Precision|Precision|Precision|Scale (1:0)|Scale (1:0)|Size|Size|Size|
|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|Meter Value 1|
|…|…|…|…|…|…|…|…|
|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|Meter Value N|
|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|Scale 2|



For fields description, refer to Section 2.2.59.3 Meter Report Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 297