<!-- PAGE 707 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.25** **Indicator** **Command** **Class,** **version** **1**


The Indicator Command Class is used to help end users to monitor the operation or condition of the
application provided by a supporting node.


**3.2.25.1** **Interoperability** **considerations**


Version 1 supporting nodes implement a single indicator resource. The indicator resource can only be
turned on or off.


Nodes supporting the Wake-Up Command Class SHOULD keep the indicator in the same state
(On/Off) as last instructed by an Indicator Set Command.


**3.2.25.2** **Indicator** **Set** **Command**


This command is used to enable or disable the indicator resource.


Table 3.106: Indicator Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|
|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|
|Value|Value|Value|Value|Value|Value|Value|Value|



**Value** **(8** **bits)**

This field is used to enable or disable the indicator resource.

This field MUST be in the range 0x00..0x63 or 0xFF.

The value 0x00 MUST indicate that the indicator MUST be turned off/disabled.


Values in the range 0x01..0x63 MUST indicate that the indicator MUST be turned on/enabled.


The value 0xFF MUST indicate that the indicator MUST be turned on/enabled.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 706




<!-- PAGE 708 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.25.3** **Indicator** **Get** **Command**


This command is used to request the state of the indicator resource.


The Indicator Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.107: Indicator Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|
|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|



**3.2.25.4** **Indicator** **Report** **Command**


This command is used to advertise the current state of the indicator resource.


Table 3.108: Indicator Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|
|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|
|Value|Value|Value|Value|Value|Value|Value|Value|



**Value** **(8** **bits)**

This field is used to advertise the current state of the indicator resource. This field MUST be in the
range 0x00..0x63 or set to 0xFF.

The value 0x00 MUST indicate that the indicator is turned off/disabled.


Values in the range 0x01..0x63 MUST indicate that the indicator is turned on/enabled.


The value 0xFF MUST indicate that the indicator is turned on/enabled.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 707

---

<!-- PAGE 709 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.26** **Indicator** **Command** **Class,** **version** **2**


The Indicator Command Class, version 2 is used to manipulate indicator resources in a supporting
node. An indicator may be an LED, an LCD display or a buzzer.


**3.2.26.1** **Compatibility** **Considerations**


The Indicator Command Class, version 1 provides a single unspecified indicator resource. Version 2
introduces support for multiple indicator resources. Each indicator resource may implement a number
of properties (or capabilities) such as turning on/off, set on a specific level or toggling state.


A controlling node may discover the supported indicators ID and their property IDs via the Indicator
Supported Report Command.

The Indicator Command Class, version 2 renames the Value field of version 1 to “Indicator 0 Value”.

The Indicator 0 Value field properties are unspecified as in version 1.


A version 2 supporting node MUST map the Indicator 0 to one of its supported Indicator ID and
Property ID. The Indicator 0 SHOULD be mapped to an indicator 0x01 (Multilevel) or 0x02 (Binary)
Property ID.


A supporting node advertising no support for the “Low power” indication Property ID and supporting
the Wake Up Command Class MUST keep awake as long as one of the property ID is not 0x00 (off)
for the actual Indicator ID. Such a node MUST return to sleep after both the Wake Up No More
Information Command is received and all Property IDs are back to 0x00 for the actual Indicator ID.


A supporting node advertising support for the “Low power” indication Property ID and supporting
the Wake Up Command Class MAY return to sleep even if an indication is ongoing for the actual
Indicator ID.


**3.2.26.2** **Interoperability** **considerations**


A supporting device MAY use its indicator resources for local status reporting.


After receiving an Indicator Set Command, a supporting node MUST NOT use its indicator resources
for local status reporting until it has completed the operation requested by the Set Command.


An exception to this MAY be interface feedback functionality like a short beep on each button press.
Likewise, transmission failure to a controlling node MAY be advertised via the use of local indications.
As an example, an entry control keypad device may feature an LCD backlight. If the backlight is
advertised as an indicator resource, a central control application also has to control the backlight of
the keypad, e.g. in response to local user activity and to temporarily draw attention to all keypads
when an alarm is enabled.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 708




<!-- PAGE 710 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.26.3** **Indicator** **Set** **Command**


This command is used to manipulate one or more indicator resources at a supporting node.


Table 3.109: Indicator Set Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|
|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|Command = INDICATOR_SET (0x01)|
|Indicator 0 Value<br>(Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value<br>(Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value<br>(Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value<br>(Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value<br>(Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value<br>(Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value<br>(Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value<br>(Indicator ID 0 = 0x00, Property ID 0 = 0x01)|
|Reserved|Reserved|Reserved|Indicator Object Count|Indicator Object Count|Indicator Object Count|Indicator Object Count|Indicator Object Count|
|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|
|Property ID 1|Property ID 1|Property ID 1|Property ID 1|Property ID 1|Property ID 1|Property ID 1|Property ID 1|
|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|
|…|…|…|…|…|…|…|…|
|Indicator ID N|Indicator ID N|Indicator ID N|Indicator ID N|Indicator ID N|Indicator ID N|Indicator ID N|Indicator ID N|
|Property ID N|Property ID N|Property ID N|Property ID N|Property ID N|Property ID N|Property ID N|Property ID N|
|Value N|Value N|Value N|Value N|Value N|Value N|Value N|Value N|



**Indicator** **0** **Value** **(8** **bits)**

This field provides backwards compatibility for version 1 supporting nodes.

A receiving node MUST ignore this field if the _Indicator_ _Object_ _Count_ field is not set to 0.


A receiving node MUST map this value to a supported indicator resource if the _Indicator Object Count_
field is set to 0 or not included in the command.


Refer to Section 3.2.26.1 Compatibility Considerations.


**Reserved**

This field MUST be set to 0 by a sending device and MUST be ignored by a receiving device.


**Indicator** **Object** **Count** **(5** **bits)**

This field is used to advertise the number of indicator objects carried in the actual command. An
indicator object MUST comprise an _Indicator_ _ID_, a _Property_ _ID_ and a _Value_ field.


**Indicator** **ID** **(8** **bits,** **N** **times)**

This field is used to identify the actual indicator resource. Indicator IDs values are defined in [24].

A receiving node MUST ignore the entire indicator object if an unsupported Indicator ID is specified.


A receiving node MUST NOT ignore other indicator objects included in the command if an unsupported Indicator ID is specified.


**Property** **ID** **(8** **bits,** **N** **times)**

This field is used to identify the specific property of the indicator resource identified by the corresponding _Indicator_ _ID_ field.


A receiving node MUST ignore the entire indicator object if an unsupported Property ID for the
corresponding Indicator ID is specified. The receiving node MUST NOT ignore other indicator objects
included in the command.

If an _Indicator_ _ID_ is specified in an object but not all _Property_ _IDs_ are included in the command, a
supporting node MUST assume non-specified Property IDs values to be set to 0x00.

If several Property IDs not belonging to the same Property group defined in [24] are specified in the
command, the Property IDs from one Property group MUST be applied and all other Property IDs
MUST be ignored. For example, if Multilevel and Binary property IDs are defined, only one Property
ID value MUST be applied and the other MUST be ignored.


Properties marked as “ADVERTISE ONLY:” MUST be ignored if received in a controlling command.


**Value** **(8** **bits,** **N** **times)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 709




<!-- PAGE 711 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to specify the value to assign to the specific indicator property identified by the
_Indicator_ _ID_ and the _Property_ _ID_ fields.

This field MUST be set according to the defined values and requirements for Property IDs in [24].


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 710




<!-- PAGE 712 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.26.4** **Indicator** **Get** **Command**


This command is used to request the state of an indicator.


The Indicator Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.110: Indicator Get Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|
|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|Command = INDICATOR_GET (0x02)|
|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|



**Indicator** **ID** **(8** **bits)**

This field is used to specify the actual indicator resource.

If an unsupported Indicator ID is specified in this command, a receiving node MUST return an
indicator object with the specified _Indicator_ _ID_ and the _Property_ _ID_ and Value fields set to 0x00.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 711




<!-- PAGE 713 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.26.5** **Indicator** **Report** **Command**


This command is used to advertise the state of an indicator resource.


Table 3.111: Indicator Report Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|
|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|Command = INDICATOR_REPORT (0x03)|
|Indicator 0 Value (Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value (Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value (Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value (Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value (Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value (Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value (Indicator ID 0 = 0x00, Property ID 0 = 0x01)|Indicator 0 Value (Indicator ID 0 = 0x00, Property ID 0 = 0x01)|
|Reserved|Reserved|Reserved|Indicator Object Count|Indicator Object Count|Indicator Object Count|Indicator Object Count|Indicator Object Count|
|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|
|Property ID 1|Property ID 1|Property ID 1|Property ID 1|Property ID 1|Property ID 1|Property ID 1|Property ID 1|
|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|Value 1|
|…|…|…|…|…|…|…|…|
|Indicator ID N|Indicator ID N|Indicator ID N|Indicator ID N|Indicator ID N|Indicator ID N|Indicator ID N|Indicator ID N|
|Property ID N|Property ID N|Property ID N|Property ID N|Property ID N|Property ID N|Property ID N|Property ID N|
|Value N|Value N|Value N|Value N|Value N|Value N|Value N|Value N|



**Indicator** **0** **Value** **(8** **bits)**

This field provides backwards compatibility for version 1 controlling nodes.


A sending node MUST advertise the current value of the mapped Indicator ID and Property ID.

A version 2 controlling node MUST ignore the Indicator 0 Value field if other values are advertised.
Refer to Section 3.2.26.1 Compatibility Considerations.


**Reserved**

This field MUST be set to 0 by a sending device and MUST be ignored by a receiving device.


**Indicator** **Object** **Count** **(5** **bits)**

This field is used to advertise the number of indicator objects carried in this command. An indicator
object MUST comprise an _Indicator_ _ID_, a _Property_ _ID_ and a _Value_ field.


**Indicator** **ID** **(N** **bytes)**

This field is used to identify the actual indicator resource.


All indicator objects MUST carry the same Indicator ID.


**Property** **ID** **(N** **bytes)**

This field is used to identify the specific property of the indicator resource identified by the corresponding _Indicator_ _ID_ field.


If not all Property IDs are included in the command for the actual Indicator ID, a controlling node
MUST assume non-specified Property IDs values to be 0x00.

**Value** **(N** **bytes)** This field is used to specify the current value of the specific indicator property
identified by the _Indicator_ _ID_ and the _Property_ _ID_ fields.

This field MUST be set according to the defined values for Property IDs in [24].


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 712




<!-- PAGE 714 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.26.6** **Indicator** **Supported** **Get** **Command**


This command is used to request the supported properties of an indicator.


The Indicator Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.112: Indicator Supported Get Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|
|Command = INDICATOR_SUPPORTED_GET (0x04)|Command = INDICATOR_SUPPORTED_GET (0x04)|Command = INDICATOR_SUPPORTED_GET (0x04)|Command = INDICATOR_SUPPORTED_GET (0x04)|Command = INDICATOR_SUPPORTED_GET (0x04)|Command = INDICATOR_SUPPORTED_GET (0x04)|Command = INDICATOR_SUPPORTED_GET (0x04)|Command = INDICATOR_SUPPORTED_GET (0x04)|
|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|



**Indicator** **ID** **(1** **byte)**

This field is used to specify the actual indicator resource.

A controlling node SHOULD set this field to zero to discover the supported Indicator IDs. A supporting node receiving this field set to 0x00 MUST advertise the first supported Indicator ID in

response.

A supporting node receiving a non-zero Indicator ID that is not supported MUST set all fields ( _Indi-_
_cator_ _ID_, _Next_ _Indicator_ _ID_, _Property_ _Supported_ _Bit_ _Mask_ _Length_ ) to 0x00 in the returned response.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 713




<!-- PAGE 715 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.26.7** **Indicator** **Supported** **Report** **Command**


This command is used to advertise the supported properties for a given indicator.


Table 3.113: Indicator Supported Report Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|
|Command = INDICATOR_SUPPORTED_REPORT (0x05)|Command = INDICATOR_SUPPORTED_REPORT (0x05)|Command = INDICATOR_SUPPORTED_REPORT (0x05)|Command = INDICATOR_SUPPORTED_REPORT (0x05)|Command = INDICATOR_SUPPORTED_REPORT (0x05)|Command = INDICATOR_SUPPORTED_REPORT (0x05)|Command = INDICATOR_SUPPORTED_REPORT (0x05)|Command = INDICATOR_SUPPORTED_REPORT (0x05)|
|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|
|Next Indicator ID|Next Indicator ID|Next Indicator ID|Next Indicator ID|Next Indicator ID|Next Indicator ID|Next Indicator ID|Next Indicator ID|
|Reserved|Reserved|Reserved|Property Supported Bit Mask Length|Property Supported Bit Mask Length|Property Supported Bit Mask Length|Property Supported Bit Mask Length|Property Supported Bit Mask Length|
|Property Supported Bit Mask 1|Property Supported Bit Mask 1|Property Supported Bit Mask 1|Property Supported Bit Mask 1|Property Supported Bit Mask 1|Property Supported Bit Mask 1|Property Supported Bit Mask 1|Property Supported Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Property Supported Bit Mask N|Property Supported Bit Mask N|Property Supported Bit Mask N|Property Supported Bit Mask N|Property Supported Bit Mask N|Property Supported Bit Mask N|Property Supported Bit Mask N|Property Supported Bit Mask N|



**Indicator** **ID** **(1** **byte)**

This field is used to specify the actual indicator ID resource for the supported properties are being
advertised.

The supported Indicator IDs MUST be according to the Indicator IDs values defined in [24].


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Next** **Indicator** **ID** **(8** **bits)**

This field is used to advertise if more Indicator IDs are supported after the actual Indicator ID
advertised by the _Indicator_ _ID_ field.

If a sending node supports additional Indicator IDs, this field MUST advertise the next supported
Indicator ID.

If the sending node does not support additional Indicator IDs this field MUST be set to 0x00.

The supported Indicator IDs MUST be according to the Indicator IDs values defined in [24].


**Property** **Supported** **Bit** **Mask** **Length** **(5** **bits)**

This field is used to advertise the length of the _Property_ _Supported_ _Bit_ _Mask_ field in bytes.


The value MUST be in the range 0..32.


**Property** **Supported** **Bit** **Mask** **(N** **bytes)**

This field is used to advertise the properties supported by the actual Indicator ID.

The length of this field in bytes MUST be according to the _Property_ _Supported_ _Bit_ _Mask_ _Length_ field
value. This field MUST be encoded as a bitmask as follow:


 - Bit 0 in Bit Mask 1 is not allocated to any property and MUST be set to zero.


 - Bit 1 in Bit Mask 1 MUST indicate if Property ID = 1 (Multilevel) is supported.

 - Bit 2 in Bit Mask 1 MUST indicate if Property ID = 2 (On/Off) is supported.


 - …


If the Property ID is supported, the corresponding bit MUST be set to 1.


If the Property ID is not supported the corresponding bit MUST be set to 0.

The supported Property IDs MUST be according to the Property IDs values defined in [24].


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 714

---

<!-- PAGE 716 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.27** **Indicator** **Command** **Class,** **version** **3**


The Indicator Command Class, version 3 is used to manipulate indicator resources in a supporting
node. An indicator may be an LED, an LCD display or a buzzer.


**3.2.27.1** **Compatibility** **Considerations**


The Indicator Command Class, version 3 is backwards compatible with the Indicator Command Class,
version 2. All commands and fields not mentioned in this version MUST remain unchanged from the
Indicator Command Class, version 2.


This version introduces new Indicator IDs and Property IDs. The list of supported Indicator IDs and
Property IDs is moved to [24]. Values not defined in [24] are reserved and MUST NOT be used by a
supporting node.


New values MAY be added to [24] and will be labelled under version 3.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 715

---

<!-- PAGE 717 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.28** **Indicator** **Command** **Class,** **version** **4**


**3.2.28.1** **Compatibility** **Considerations**


The Indicator Command Class, version 4 is backwards compatible with the Indicator Command Class,
version 3. All commands and fields not mentioned in this version MUST remain unchanged from the
Indicator Command Class, version 3.


This version introduces 2 new commands used to request the detailed information, appearance and
use of manufacturer defined Indicator IDs.


 - Indicator Description Get Command


 - Indicator Description Report Command

Supporting nodes supporting Indicator IDs in the range 0x80..0x9F (manufacturer defined indicators)
MUST have a description available that can be requested via the version 4 commands.


Indicator IDs in the range 0x80..0x9F that are supported by a node MUST NOT replace or be
achievable by any combination of Indicator IDs defined in [24].


**3.2.28.2** **Indicator** **Description** **Get** **Command**


This command is used to request a detailed description of the appearance and use of an Indicator ID


The Indicator Description Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.114: Indicator Description Get Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|
|Command = INDICATOR_DESCRIPTION_GET (0x06)|Command = INDICATOR_DESCRIPTION_GET (0x06)|Command = INDICATOR_DESCRIPTION_GET (0x06)|Command = INDICATOR_DESCRIPTION_GET (0x06)|Command = INDICATOR_DESCRIPTION_GET (0x06)|Command = INDICATOR_DESCRIPTION_GET (0x06)|Command = INDICATOR_DESCRIPTION_GET (0x06)|Command = INDICATOR_DESCRIPTION_GET (0x06)|
|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|Indicator ID|



**Indicator** **ID** **(8** **bits)**

This field is used to specify the actual indicator resource.

A supporting node MUST return a report for the Indicator ID value specified in this field.

This field MUST be in the range 0x80..0x9F.


A supporting node receiving this command for an Indicator ID outside the 0x80..0x9F range MUST
return an Indicator Description Report with the Description Length set to 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 716




<!-- PAGE 718 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.28.3** **Indicator** **Description** **Report** **Command**


This command is used to advertise appearance and use of an indicator ID resource.


Table 3.115: Indicator Description Report Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|Command Class = COMMAND_CLASS_INDICATOR (0x87)|
|Command = INDICATOR_DESCRIPTION_REPORT (0x07)|Command = INDICATOR_DESCRIPTION_REPORT (0x07)|Command = INDICATOR_DESCRIPTION_REPORT (0x07)|Command = INDICATOR_DESCRIPTION_REPORT (0x07)|Command = INDICATOR_DESCRIPTION_REPORT (0x07)|Command = INDICATOR_DESCRIPTION_REPORT (0x07)|Command = INDICATOR_DESCRIPTION_REPORT (0x07)|Command = INDICATOR_DESCRIPTION_REPORT (0x07)|
|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|Indicator ID 1|
|Description Length|Description Length|Description Length|Description Length|Description Length|Description Length|Description Length|Description Length|
|Description 1|Description 1|Description 1|Description 1|Description 1|Description 1|Description 1|Description 1|
|…|…|…|…|…|…|…|…|
|Description N|Description N|Description N|Description N|Description N|Description N|Description N|Description N|



**Indicator** **ID** **(8** **bits)**

This field is used to specify the actual indicator resource for which the description is being advertised.


**Description** **Length** **(1** **byte)**

This field indicates the length in bytes of the _Description_ field.


The value 0 MUST indicate that no description is available for the Indicator ID.


**Description** **(N** **bytes)**

This field is used to advertise the appearance and use of the Indicator ID.

It MUST replace the “Appearance and use” column information from [24] for manufacturer defined
Indicator IDs.

The length of this field in bytes MUST comply with the advertised value in the _Description_ _Length_
field.

This field MUST be omitted if the _Description_ _Length_ field is set to 0.

This field MUST be encoded in UTF-8 format.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 717